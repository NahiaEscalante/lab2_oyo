"""Gráfica de 1/d_o vs 1/d_i (Cuadro 1): la intersección con el eje vertical es 1/f."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

do = np.array([49.2, 54.2, 59.2, 64.2, 69.2, 74.2, 99.2])
di = np.array([31.7, 29.7, 28.2, 27.2, 26.1, 26.2, 23.9])
x, y = 1/di, 1/do
n = len(x)
A = np.vstack([x, np.ones(n)]).T
(m, b), *_ = np.linalg.lstsq(A, y, rcond=None)
yp = m*x + b
r2 = 1 - ((y - yp)**2).sum()/((y - y.mean())**2).sum()
s = np.sqrt(((y - yp)**2).sum()/(n - 2)); sxx = ((x - x.mean())**2).sum()
sm = s/np.sqrt(sxx); sb = s*np.sqrt(1/n + x.mean()**2/sxx)
f = 1/b; sf = sb/b**2
print("tabla:"); [print(f"{a:.1f} {c:.1f} {1/a:.5f} {1/c:.5f}") for a, c in zip(do, di)]
print(f"m={m:.4f}±{sm:.4f} b={b:.5f}±{sb:.5f} R2={r2:.4f} f={f:.2f}±{sf:.2f} R={2*f:.2f}±{2*sf:.2f} err={abs(f-20)/20*100:.1f}%")

fig, ax = plt.subplots(figsize=(6.4, 4.4), dpi=200)
xx = np.linspace(0, x.min(), 50)
ax.plot(xx, m*xx + b, color="#1f4e79", lw=1.5, ls="--", label="Extrapolación hasta $1/d_i = 0$")
xx = np.linspace(x.min(), 0.045, 50)
ax.plot(xx, m*xx + b, color="#1f4e79", lw=2,
        label=f"Ajuste: $1/d_o$ = {m:.3f}$\\cdot(1/d_i)$ + {b:.4f}  ($R^2$ = {r2:.3f})")
xx = np.linspace(0, 0.045, 50)
ax.plot(xx, -xx + 1/20, color="#888888", lw=1.5, ls=":", label="Teoría ($f$ = 20 cm): $1/d_o = -1/d_i + 0.05$")
ax.scatter(x, y, s=40, color="#d1495b", zorder=3, edgecolor="white", linewidth=1, label="Datos experimentales")
ax.plot(0, b, "o", ms=9, mfc="none", mec="black", mew=1.5, zorder=4)
ax.annotate(f"Intersección con el eje vertical:\n$1/f$ = {b:.4f} cm$^{{-1}}$  →  $f$ = {f:.2f} cm",
            xy=(0, b), xytext=(0.004, 0.012), fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color="black", lw=1))
ax.set_xlim(0, 0.045); ax.set_ylim(0, 0.058)
ax.set_xlabel("$1/d_i$ (cm$^{-1}$)"); ax.set_ylabel("$1/d_o$ (cm$^{-1}$)")
ax.grid(alpha=.25); [ax.spines[k].set_visible(False) for k in ("top", "right")]
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("Inversas de las distancias — espejo cóncavo", fontsize=10)
fig.tight_layout(); fig.savefig("grafico_inversas.png")
