import cv2, numpy as np, sys
src, dst, mode = sys.argv[1], sys.argv[2], sys.argv[3]
img = cv2.imread(src); H, W = img.shape[:2]
if mode == "warp":
    k = 1000 / max(H, W); small = cv2.resize(img, None, fx=k, fy=k)
    g = cv2.GaussianBlur(cv2.cvtColor(small, cv2.COLOR_BGR2GRAY), (5,5), 0)
    _, th = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, np.ones((15,15), np.uint8))
    c = max(cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea)
    for eps in np.linspace(0.01, 0.08, 15):
        a = cv2.approxPolyDP(c, eps * cv2.arcLength(c, True), True)
        if len(a) == 4: break
    q = a.reshape(4,2).astype(np.float32) / k
    s = q.sum(1); d = np.diff(q, axis=1).ravel()
    tl, br, tr, bl = q[s.argmin()], q[s.argmax()], q[d.argmin()], q[d.argmax()]
    w = int(max(np.linalg.norm(tr-tl), np.linalg.norm(br-bl))); h = int(w*297/210)
    img = cv2.warpPerspective(img, cv2.getPerspectiveTransform(np.float32([tl,tr,br,bl]), np.float32([[0,0],[w,0],[w,h],[0,h]])), (w,h))
# normalizar iluminación por canal
chs = []
for ch in cv2.split(img):
    bg = cv2.GaussianBlur(cv2.morphologyEx(ch, cv2.MORPH_CLOSE, np.ones((25,25), np.uint8)), (0,0), 25)
    chs.append(cv2.divide(ch, bg, scale=255))
n = cv2.merge(chs).astype(np.float32)
# niveles: negro=110, blanco=228, gamma para oscurecer trazos
lo, hi = 110., 228.
n = np.clip((n - lo) / (hi - lo), 0, 1) ** 1.4 * 255
n = n.astype(np.uint8)
n[n.min(axis=2) > 215] = 255
cv2.imwrite(dst, n, [cv2.IMWRITE_JPEG_QUALITY, 92])
