"""Animaciones para el video del Laboratorio 2 (MP4, 1920x1080, 30 fps).

A1  Objeto acercándose a un espejo cóncavo (trazado de rayos, teoría con f = 20 cm)
A3  Construcción de la recta de inversas con los datos del Cuadro 1
A4  Efecto del caso d_o = R en la recta de inversas
A5  Desfase sistemático delta: la recta experimental se desliza hacia la teórica

Uso:  python3 figuras/animaciones.py            (genera las cuatro en animaciones/)
      python3 figuras/animaciones.py A3 A4      (solo las indicadas)
"""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "animaciones")
os.makedirs(OUT, exist_ok=True)
FPS = 30

# Paleta (referencia dataviz): datos azul, caso descartado naranja + rombo (codificación doble)
SURF = "#fcfcfb"; INK = "#1f1f1e"; INK2 = "#5c5b55"; GRID = "#e4e3de"
BLUE = "#2a78d6"; ORANGE = "#eb6834"; TEAL = "#1baf7a"; GRAY = "#9a998f"

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "font.size": 20, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
    "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1, "lines.linewidth": 3,
})

# Datos del Cuadro 1 (hoja firmada) y caso d_o = R del Cuadro 2
DO = np.array([49.2, 54.2, 59.2, 64.2, 69.2, 74.2, 99.2])
DI = np.array([31.7, 29.7, 28.2, 27.2, 26.1, 26.2, 23.9])
DO_R, DI_R = 40.0, 27.4


def ajuste(x, y):
    n = len(x); m, b = np.polyfit(x, y, 1); r = y - (m*x + b)
    s = np.sqrt((r**2).sum()/(n - 2)); sxx = ((x - x.mean())**2).sum()
    sb = s*np.sqrt(1/n + x.mean()**2/sxx)
    r2 = 1 - (r**2).sum()/((y - y.mean())**2).sum()
    return m, b, sb, r2


def guardar(anim, nombre, frames):
    ruta = os.path.join(OUT, nombre)
    anim.save(ruta, writer=FFMpegWriter(fps=FPS, bitrate=6000), dpi=120)
    print(f"{nombre}: {frames/FPS:.1f} s -> {ruta}")


def ease(t):
    t = np.clip(t, 0, 1); return t*t*(3 - 2*t)


# ---------------------------------------------------------------- A1
def a1_concavo():
    f, R, h = 20.0, 40.0, 3.0
    fig, ax = plt.subplots(figsize=(16, 9))
    fig.subplots_adjust(left=0.03, right=0.97, top=0.86, bottom=0.06)
    # trayectoria de d_o: 75 -> 9 cm, con pausas en los casos de la guía
    claves = [(75, 1.0), (45, 2.2), (45, 1.2), (40, 1.0), (40, 1.4), (35, 1.0), (35, 1.4),
              (20, 1.6), (20, 1.4), (12, 1.2), (12, 2.0)]
    tray = []
    for (a, _), (b, dur) in zip(claves[:-1], claves[1:]):
        n = int(dur*FPS); tray += list(a + (b - a)*ease(np.linspace(0, 1, n)))
    frames = len(tray)

    def caso(do):
        if abs(do - f) < 0.6: return "$d_o = f$: rayos reflejados paralelos, imagen en el infinito"
        if abs(do - R) < 0.6: return "$d_o = R$: real, invertida, del mismo tamaño"
        if do > R: return "$d_o > R$: real, invertida, reducida"
        if do > f: return "$f < d_o < R$: real, invertida, ampliada"
        return "$d_o < f$: virtual, derecha, ampliada (detrás del espejo)"

    def dibujar(i):
        ax.clear(); do = tray[i]
        ax.set_xlim(-110, 70); ax.set_ylim(-13, 13); ax.set_aspect("auto")
        ax.axis("off")
        ax.axhline(0, color=INK2, lw=1.5)
        yy = np.linspace(-11, 11, 100); ax.plot(-R + np.sqrt(R**2 - yy**2) - 0, yy, color=INK, lw=5)
        ax.plot(-R + np.sqrt(R**2 - yy**2) + 0.9, yy, color=INK2, lw=1, ls=(0, (2, 3)))
        for x, lab in [(-f, "F"), (-R, "C")]:
            ax.plot(x, 0, "o", color=INK, ms=9); ax.text(x, -1.6, lab, ha="center", fontsize=22, color=INK)
        ax.annotate("", xy=(-do, h), xytext=(-do, 0), arrowprops=dict(arrowstyle="-|>", lw=4, color=BLUE, mutation_scale=30))
        ax.text(-do, h + 1.0, "objeto", ha="center", color=BLUE, fontsize=18)
        L = -110
        # rayo 1: paralelo, se refleja pasando por F
        ax.plot([-do, 0], [h, h], color=INK2, lw=2)
        s1 = h/f  # pendiente del reflejado hacia la izquierda: pasa por (-f,0)
        ax.plot([0, L], [h, h + s1*L], color=INK2, lw=2)
        # rayo 3: central, al vértice y simétrico
        ax.plot([-do, 0], [h, 0], color=TEAL, lw=2)
        ax.plot([0, L], [0, -h/do*(-L)], color=TEAL, lw=2)
        if abs(do - f) >= 0.6:
            di = do*f/(do - f); hi = -h*di/do
            # rayo 2: focal (o en línea con F), sale paralelo
            y2 = -h*f/(do - f)
            ax.plot([-do, 0], [h, y2], color=ORANGE, lw=2)
            ax.plot([0, L], [y2, y2], color=ORANGE, lw=2)
            if di > 0:
                if di < 110:
                    ax.annotate("", xy=(-di, hi), xytext=(-di, 0), arrowprops=dict(arrowstyle="-|>", lw=4, color=INK, mutation_scale=30))
                    ax.text(-di, hi - 1.6 if hi < 0 else hi + 0.8, "imagen real", ha="center", fontsize=18, color=INK)
            else:
                X = -di
                for y0, s in [(h, s1), (0, h/do), (y2, 0)]:
                    ax.plot([0, X], [y0, y0 + s*X], color=INK2, lw=1.5, ls=(0, (4, 4)))
                if X < 70:
                    ax.annotate("", xy=(X, min(hi, 12.5)), xytext=(X, 0), arrowprops=dict(arrowstyle="-|>", lw=4, color=INK, mutation_scale=30, linestyle="--"))
                    ax.text(X, min(hi, 12.5) + 0.5, "imagen virtual", ha="center", fontsize=18, color=INK)
            dtxt = f"$d_o$ = {do:4.1f} cm    $d_i$ = {di:6.1f} cm    $M$ = {-di/do:+.2f}"
        else:
            dtxt = f"$d_o$ = {do:4.1f} cm    $d_i \\to \\infty$"
        fig.suptitle("Espejo cóncavo ($f$ = 20 cm): el objeto se acerca", fontsize=28, color=INK, y=0.97)
        ax.text(0.5, 1.02, caso(do), transform=ax.transAxes, ha="center", fontsize=24, color=INK)
        ax.text(0.02, 0.03, dtxt, transform=ax.transAxes, fontsize=20, color=INK2, zorder=5,
                bbox=dict(boxstyle="round,pad=0.4", facecolor=SURF, edgecolor="none"))
        ax.text(0.98, 0.03, "Teoría: ecuación del espejo", transform=ax.transAxes, ha="right", fontsize=16, color=GRAY)

    guardar(FuncAnimation(fig, dibujar, frames=frames), "A1_objeto_acercandose_concavo.mp4", frames)
    plt.close(fig)


# ---------------------------------------------------------------- base para A3-A5
def ejes_inversas(ax, titulo):
    ax.set_xlim(0, 0.046); ax.set_ylim(0, 0.058)
    ax.set_xlabel("$1/d_i$  (cm$^{-1}$)"); ax.set_ylabel("$1/d_o$  (cm$^{-1}$)")
    ax.set_title(titulo, fontsize=26, color=INK, pad=18)


# ---------------------------------------------------------------- A3
def a3_inversas():
    x, y = 1/DI, 1/DO; m, b, sb, r2 = ajuste(x, y)
    fig, ax = plt.subplots(figsize=(16, 9)); fig.subplots_adjust(left=0.1, right=0.96, top=0.88, bottom=0.12)
    t_pts, t_fit, t_ext, t_teo, t_end = 0.7*7, 1.5, 2.0, 1.2, 3.0
    T = t_pts + t_fit + t_ext + t_teo + t_end; frames = int(T*FPS)

    def dibujar(i):
        t = i/FPS; ax.clear(); ejes_inversas(ax, "Recta de inversas con los datos del Cuadro 1")
        k = min(7, int(t/0.7) + 1)
        ax.scatter(x[:k], y[:k], s=160, color=BLUE, edgecolor=SURF, linewidth=2, zorder=3, label="Datos (Cuadro 1)")
        ax.text(0.98, 0.95, f"Puntos: {k}/7", transform=ax.transAxes, ha="right", fontsize=20, color=INK2)
        t1 = t - t_pts
        if t1 > 0:
            p = ease(t1/t_fit); xa = np.linspace(x.min(), x.min() + p*(x.max() - x.min()), 50)
            ax.plot(xa, m*xa + b, color=INK, lw=3, label=f"Ajuste: pendiente {m:.3f}, $R^2$ = {r2:.3f}")
        t2 = t1 - t_fit
        if t2 > 0:
            p = ease(t2/t_ext); x0 = x.min()*(1 - p)
            xe = np.linspace(x0, x.min(), 30); ax.plot(xe, m*xe + b, color=INK, lw=2.5, ls=(0, (6, 4)))
            if p >= 1:
                ax.plot(0, b, "o", ms=16, color=ORANGE, zorder=4, clip_on=False)
                ax.annotate(f"corte: $1/f$ = {b:.4f} cm$^{{-1}}$\n$f$ = {1/b:.2f} ± {sb/b**2:.2f} cm",
                            xy=(0, b), xytext=(0.004, 0.020), fontsize=22, color=INK,
                            arrowprops=dict(arrowstyle="->", lw=2, color=INK))
        t3 = t2 - t_ext
        if t3 > 0:
            xx = np.linspace(0, 0.046, 50)
            ax.plot(xx, -xx + 1/20, color=GRAY, lw=2.5, ls=":", alpha=ease(t3/t_teo), label="Teoría ($f$ = 20 cm)")
        ax.legend(loc="upper right", bbox_to_anchor=(1, 0.9), frameon=False, fontsize=18)

    guardar(FuncAnimation(fig, dibujar, frames=frames), "A3_recta_inversas.mp4", frames)
    plt.close(fig)


# ---------------------------------------------------------------- A4
def a4_descarte():
    x, y = 1/DI, 1/DO; xR, yR = 1/DI_R, 1/DO_R
    m7, b7, _, r7 = ajuste(x, y); m8, b8, _, r8 = ajuste(np.append(x, xR), np.append(y, yR))
    fig, ax = plt.subplots(figsize=(16, 9)); fig.subplots_adjust(left=0.1, right=0.96, top=0.88, bottom=0.12)
    fases = [("sin", 2.0), ("entra", 1.5), ("con", 3.0), ("sale", 1.5), ("fin", 2.5)]
    lim = np.cumsum([d for _, d in fases]); frames = int(lim[-1]*FPS)

    def dibujar(i):
        t = i/FPS; ax.clear(); ejes_inversas(ax, "¿Encaja el caso $d_o = R$ con los demás puntos?")
        k = int(np.searchsorted(lim, t, side="right")); fase = fases[min(k, 4)][0]
        t0 = 0 if k == 0 else lim[k - 1]; p = ease((t - t0)/fases[min(k, 4)][1])
        w = {"sin": 0, "entra": p, "con": 1, "sale": 1 - p, "fin": 0}[fase]
        m, b = m7 + w*(m8 - m7), b7 + w*(b8 - b7); r2 = r7 + w*(r8 - r7)
        xx = np.linspace(0.028, 0.045, 50)
        ax.plot(xx, m*xx + b, color=INK, lw=3)
        ax.scatter(x, y, s=160, color=BLUE, edgecolor=SURF, linewidth=2, zorder=3, label="Cuadro 1 (7 puntos)")
        if fase in ("entra", "con", "sale"):
            a = w if fase != "sale" else 1
            ax.scatter([xR], [yR], s=320, marker="D", color=ORANGE, edgecolor=INK, linewidth=1.5, zorder=4,
                       alpha=a if fase == "entra" else 1, label="Caso $d_o = R$ (40; 27.4 cm)")
        elif fase == "fin":
            ax.scatter([xR], [yR], s=320, marker="D", facecolor="none", edgecolor=ORANGE, linewidth=2.5, zorder=4,
                       label="Caso $d_o = R$ (descartado)")
        ax.text(0.03, 0.12, f"$R^2$ = {r2:.3f}", transform=ax.transAxes, fontsize=34, color=INK)
        ax.legend(loc="upper right", frameon=False, fontsize=18)
        if fase == "con":
            ax.text(0.03, 0.04, "La recta deja de pasar por los demás puntos", transform=ax.transAxes, fontsize=20, color=INK2)
        if fase == "fin":
            ax.text(0.03, 0.04, "Sin él, la recta vuelve a pasar por los siete puntos", transform=ax.transAxes, fontsize=20, color=INK2)

    guardar(FuncAnimation(fig, dibujar, frames=frames), "A4_descarte_dR.mp4", frames)
    plt.close(fig)


# ---------------------------------------------------------------- A5
def a5_desfase():
    fig, ax = plt.subplots(figsize=(16, 9)); fig.subplots_adjust(left=0.1, right=0.96, top=0.88, bottom=0.12)
    t_ini, t_mov, t_fin = 1.5, 4.0, 3.0; frames = int((t_ini + t_mov + t_fin)*FPS)

    def dibujar(i):
        t = i/FPS; d = 1.4*ease((t - t_ini)/t_mov)
        x, y = 1/(DI + d), 1/(DO + d); m, b, _, _ = ajuste(x, y)
        fk = (1/(1/(DO + d) + 1/(DI + d))).mean()
        ax.clear(); ejes_inversas(ax, "Hipótesis: un mismo desfase $\\delta$ en todas las distancias")
        ax.set_xlim(0.026, 0.044); ax.set_ylim(0.006, 0.026)
        xx = np.linspace(0.026, 0.044, 50)
        ax.plot(xx, -xx + 1/20, color=GRAY, lw=3, ls=":", label="Teoría ($f$ = 20 cm)")
        ax.plot(xx, m*xx + b, color=INK, lw=3, label="Ajuste")
        ax.scatter(x, y, s=160, color=BLUE, edgecolor=SURF, linewidth=2, zorder=3, label="Datos + $\\delta$")
        ax.text(0.03, 0.14, f"$\\delta$ = {d:.2f} cm", transform=ax.transAxes, fontsize=34, color=INK)
        ax.text(0.03, 0.05, f"$f$ (promedio de los $f_k$) = {fk:.2f} cm", transform=ax.transAxes, fontsize=24, color=INK2)
        ax.legend(loc="upper right", frameon=False, fontsize=18)

    guardar(FuncAnimation(fig, dibujar, frames=frames), "A5_desfase_delta.mp4", frames)
    plt.close(fig)


if __name__ == "__main__":
    todas = {"A1": a1_concavo, "A3": a3_inversas, "A4": a4_descarte, "A5": a5_desfase}
    for k in (sys.argv[1:] or todas):
        todas[k]()
