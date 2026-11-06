import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
out="/Users/nahiaescalante/Documents/UTEC/Optica/Lab2/figuras/"
do=np.array([49.2,54.2,59.2,64.2,69.2,74.2,99.2])
di=np.array([31.7,29.7,28.2,27.2,26.1,26.2,23.9])
hi=np.array([1.2,1.0,0.8,0.6,0.6,0.6,0.4]); ho=2.0
M=hi/ho
fi=1/(1/do+1/di); print("f_i",fi.round(3),"mean",fi.mean().round(3),"std",fi.std(ddof=1).round(3),"sem",(fi.std(ddof=1)/np.sqrt(7)).round(3))
def fit(x,y,lab):
    A=np.vstack([x,np.ones_like(x)]).T; (a,b),res,_,_=np.linalg.lstsq(A,y,rcond=None)
    yp=a*x+b; r2=1-((y-yp)**2).sum()/((y-y.mean())**2).sum()
    n=len(x); s=np.sqrt(((y-yp)**2).sum()/(n-2)); sxx=((x-x.mean())**2).sum()
    sa=s/np.sqrt(sxx); sb=s*np.sqrt(1/n+x.mean()**2/sxx)
    f=1/a; sf=sa/a**2
    print(lab,"a=%.5f±%.5f b=%.4f±%.4f R2=%.4f r=%.4f f=1/a=%.2f±%.2f R=%.2f±%.2f err_f=%.1f%%"%(a,sa,b,sb,r2,np.corrcoef(x,y)[0,1],f,sf,2*f,2*sf,abs(f-20)/20*100))
    return a,b,r2
print("M -di/do",(di/do).round(3))
a,b,r2=fit(di,M,"|M|=hi/ho vs di")
a2,b2,r22=fit(di,di/do,"|M|=di/do vs di")
# constrained fit intercept=-1: |M|+1 = di/f
k=(di*(M+1)).sum()/(di*di).sum(); print("constrained f=",1/k)
# 1/do vs 1/di
x=1/di; y=1/do; A=np.vstack([x,np.ones_like(x)]).T; (p,q),*_=np.linalg.lstsq(A,y,rcond=None)
print("1/do = %.4f(1/di)+%.5f -> f=%.2f"%(p,q,1/q), "R2",np.corrcoef(x,y)[0,1]**2)
# tabla 2
f=19.18
for d0,dexp in [(45,33.5),(40,27.4),(35,48.1),(15,None)]:
    dt=d0*f/(d0-f); Mt=-dt/d0
    print(d0,dexp,"di_t=%.2f M_t=%.3f"%(dt,Mt), "" if dexp is None else "Mexp=%.3f diff=%.2f%%"%(-dexp/d0,abs(dexp-dt)/dt*100))
fig,ax=plt.subplots(figsize=(6.4,4.2),dpi=200)
xx=np.linspace(22,34,50)
ax.plot(xx,a*xx+b,color="#1f4e79",lw=2,label=f"Ajuste: M = {a:.4f}·d_i − {abs(b):.3f}  (R² = {r2:.3f})")
ax.plot(xx,xx/20-1,color="#888888",lw=1.5,ls="--",label="Teoría (f = 20 cm): M = d_i/20 − 1")
ax.scatter(di,M,s=40,color="#d1495b",zorder=3,edgecolor="white",linewidth=1,label="Datos experimentales")
ax.set_xlabel("Distancia imagen $d_i$ (cm)"); ax.set_ylabel("$M = h_i/h_o$ (magnitud)")
ax.grid(alpha=.25); [ax.spines[s].set_visible(False) for s in ("top","right")]
ax.legend(frameon=False,fontsize=8,loc="upper left"); ax.set_title("Magnificación vs distancia imagen — espejo cóncavo",fontsize=10)
fig.tight_layout(); fig.savefig(out+"grafico_M_vs_di.png")
