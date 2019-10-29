
import numpy as np
import PhyPraKit as ppk
import matplotlib.pyplot as plt

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc

def loadCSV():
    hlines, data = ppk.readCSV("HandyPendel.csv")
    data = np.array(data)
    t,ax,ay,az,at=np.split(data,5)
    t = t[0]
    ax = ax[0]
    ay = ay[0]
    az = az[0]
    at = at[0]
    return t,ax,ay,az,at;

def minmaxfind(a):
    HP = np.array([])
    TP = np.array([])
    l = len(a)
    j = a[0]
    HPisNext = 1
    for k in np.arange(1,l):
        i=a[k]
        if HPisNext == 1:
            if j>i:
                HP = np.hstack((HP,k-1))
                HPisNext=0
        elif HPisNext == 0:
            if j<i:
                TP = np.hstack((TP,k-1))
                HPisNext=1
        j=a[k]
    HP=np.int_(HP)
    TP=np.int_(TP)
    return HP,TP;
#ini
t,ax,ay,az,at = loadCSV()
mh = 0.14174
mf = 0.01540
mges = mh+mf
meff = mh + (1.0/3.0)*mf



atcor = ppk.autocorrelate(ay)
HP,TP = minmaxfind(atcor)
#f= 1/T ; T= 2pi/w; f= w/2pi
th=t[HP]
tt=t[TP]
wlistH = np.array([])

'''
plt.plot(t,ax,label="ax")
plt.plot(t,ay,label="ay")
plt.plot(t,az,label="az")
plt.xlabel("t in [s]")
plt.ylabel("a in [m/s²]")
plt.legend()
plt.show()
plt.clf()

plt.plot(t,atcor)
plt.plot(t,ay)
plt.title("Autokorrelation")
plt.xlabel("t in [s]")
plt.ylabel("a in [m/s²]")
plt.show()
plt.clf()
'''

for i in np.arange(1,len(th)):
    T=th[i]-th[i-1]
    wi=2*np.pi/T
    wlistH = np.hstack((wlistH,wi))

wlistT = np.array([])
for i in np.arange(1,len(tt)):
    T=tt[i]-tt[i-1]
    wi=2*np.pi/T
    wlistT = np.hstack((wlistT,wi))


wlist = np.hstack((wlistT,wlistH))
#wlist = wlistH
w = np.mean(wlist)
wer = np.std(wlist)/np.sqrt(len(wlist))

Tlist= (2*np.pi)/wlist
T = np.mean(Tlist)
Ter = np.std(Tlist)/np.sqrt(len(Tlist))

flist= wlist/(2*np.pi)
f = np.mean(flist)
fer = np.std(flist)/np.sqrt(len(flist))

D = (w**2)*meff

wu = uc.ufloat(w,wer)
Tu = uc.ufloat(T,Ter)
fu = uc.ufloat(f,fer)
mhu = uc.ufloat(mh,0.0001)
mfu = uc.ufloat(mf,0.0001)
meffu = mhu + (1.0/3.0)*mfu
Du = (wu**2)*meffu
Dut = ((2*np.pi/Tu)**2)*meffu
print("T is: ", Tu) 
print("f is: ", fu)
print("\u03C9 is: \U0001F923", wu)
print("D is: ", Du)
#Aufgabe b
print("Aus Fit folgt: g=9,807m/s \u00B1 0,082m/s") # folgt weiter unten

dmg, dxcm = np.loadtxt("Messtabelle.txt", unpack=True)
dm = dmg/1000
dx = dxcm/100
#dmu = uc.ufloat(dm,0.0001)
#dxu = uc.ufloat(dx,0.002)
def si(m,g):
    s=(g*m)/14.637541083
    return s

kdata = kafe.Dataset(data=(dm,dx),title = "Messtabelle")
kdata.add_error_source('y', 'simple', 0.002)
fitf = si
kfit= kafe.Fit(kdata,fitf)
kfit.do_fit()
kplot = kafe.Plot(kfit)
kplot.axis_labels = ['masse', 's']
kplot.plot_all()
#kfit.plot_correlations()
#kplot.show()
























