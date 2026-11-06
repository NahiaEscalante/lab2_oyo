"""Recta 1/d_o vs 1/d_i con y sin el caso d_o = R (Cuadro 2) para justificar su descarte."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

do = np.array([49.2, 54.2, 59.2, 64.2, 69.2, 74.2, 99.2])
di = np.array([31.7, 29.7, 28.2, 27.2, 26.1, 26.2, 23.9])
do_R, di_R = 40.0, 27.4   # caso d_o = R del Cuadro 2


def ajuste(x, y):
    n = len(x); m, b = np.polyfit(x, y, 1); yp = m*x + b
    s = np.sqrt(((y - yp)**2).sum()/(n - 2)); sxx = ((x - x.mean())**2).sum()
    sm = s/np.sqrt(sxx); sb = s*np.sqrt(1/n + x.mean()**2/sxx)
    r2 = 1 - ((y - yp)**2).sum()/((y - y.mean())**2).sum()
    return m, sm, b, sb, r2


def grafica(x, y, con_punto, nombre, titulo):
    m, sm, b, sb, r2 = ajuste(x, y)
    f, sf = 1/b, sb/b**2
    print(f"{nombre}: m={m:.3f}±{sm:.3f} b={b:.5f}±{sb:.5f} R2={r2:.4f} f={f:.2f}±{sf:.2f} err={abs(f-20)/20*100:.1f}%")
    fig, ax = plt.subplots(figsize=(6.4, 4.4), dpi=200)
    xx = np.linspace(0, 0.045, 50)
    ax.plot(xx, -xx + 1/20, color="#888888", lw=1.5, ls=":", label="Teoría ($f$ = 20 cm)")
    ax.plot(xx, m*xx + b, color="#1f4e79", lw=2,
            label=f"Ajuste: pendiente {m:.3f}, $R^2$ = {r2:.3f}, $f$ = {f:.2f} cm")
    ax.scatter(1/di, 1/do, s=40, color="#d1495b", zorder=3, edgecolor="white", linewidth=1,
               label="Cuadro 1")
    if con_punto:
        ax.scatter(1/di_R, 1/do_R, s=70, marker="D", color="#e07b39", zorder=4, edgecolor="black", linewidth=1,
                   label="Caso $d_o = R$ (Cuadro 2)")
        ax.annotate("$d_o = 40$ cm, $d_i = 27.4$ cm", xy=(1/di_R, 1/do_R), xytext=(0.02, 0.031), fontsize=8.5,
                    arrowprops=dict(arrowstyle="->", lw=1))
    else:
        ax.scatter(1/di_R, 1/do_R, s=70, marker="D", facecolor="none", edgecolor="#e07b39", linewidth=1.5, zorder=4,
                   label="Caso $d_o = R$ (descartado)")
    ax.set_xlim(0, 0.045); ax.set_ylim(0, 0.058)
    ax.set_xlabel("$1/d_i$ (cm$^{-1}$)"); ax.set_ylabel("$1/d_o$ (cm$^{-1}$)")
    ax.grid(alpha=.25); [ax.spines[k].set_visible(False) for k in ("top", "right")]
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    ax.set_title(titulo, fontsize=10)
    fig.tight_layout(); fig.savefig(nombre)


x, y = 1/di, 1/do
grafica(np.append(x, 1/di_R), np.append(y, 1/do_R), True, "inversas_con_dR.png", "Con el caso $d_o = R$")
grafica(x, y, False, "inversas_sin_dR.png", "Sin el caso $d_o = R$")
# residuo del punto respecto al ajuste sin él
m, sm, b, sb, r2 = ajuste(x, y)
res = (1/do_R) - (m/di_R + b); s = np.sqrt(((y - (m*x + b))**2).sum()/(len(x) - 2))
print(f"residuo del punto: {res:.5f}  desviación típica de los residuos: {s:.5f}  -> {abs(res)/s:.1f} s")
