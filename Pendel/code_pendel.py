import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats

#import kafe
#from kafe.function_tools import FitFunction, LaTeX, ASCII
#from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt

def loadCSV(name,hlines=1,split=2):
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def load_huge_CSV(name,hlines=1,split=7):
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b,c,d,e,f,g=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    c = c[0]
    d = d[0]
    e = e[0]
    f = f[0]
    g = g[0]
    return a,b,c,d,e,f,g,data;

def linregfunc(m,b):
    x=np.linspace(0.60,0.67,100)
    f = m*x+b
    return x,f;

def calibrate(): #berechung des offsets
    n,t = loadCSV("1_1data.csv")
    slope, intercept, r_value, p_value, std_err = stats.linregress(n,t)
    #print(slope, intercept, r_value, p_value, std_err)
    #plt.plot(n,t)
    #plt.plot(n,t,'og')
    #plt.show()
    print("Offset: ", intercept)
    return intercept;

def value_g(lr,Tphy):
    #Tphy = 2*np.pi*np.sqrt((2*L)/3*g)
    g = lr*((4*np.pi**2)/Tphy**2)
    return g;

def aufgabe12():
    rh,rM1f,rM1b,rM2f,rM2b,rM3f,rM3b,data= load_huge_CSV("1_2data.csv")
    rh = rh/100 # meter
    offset = calibrate()
    data[1:] = data[1:]/1000 # time from ms to s
    data[1:] = data[1:]-offset # offset korrektur
    '''
    for x in np.arange(1,7):    #Daten plot
        if x == 1:
            Mname = "Messreihe 1, fest"
        elif x == 2:
            Mname = "Messreihe 1, beweglich"
        elif x == 3:
            Mname = "Messreihe 2, fest"
        elif x == 4:
            Mname = "Messreihe 2, beweglich"
        elif x == 5:
            Mname = "Messreihe 3, fest"
        elif x == 6:
            Mname = "Messreihe 3, beweglich"
        plt.plot(data[0],data[x],label=Mname)
    plt.legend()
    plt.title("Messdaten")
    plt.xlabel("h in cm")
    plt.ylabel("t in s")
    plt.grid(True)
    plt.show()
    '''
    data[1:] = data[1:]/5 #Messadaten zu Perioden T
    #mitteln der Messreihen
    Tf = np.array([])
    Tb = np.array([])
    Tfstd = np.array([])
    Tbstd = np.array([])
    for i in np.arange(len(data[1])): # Mittelwerte und Standardabweichungen
        tempf = [data[1][i], data[3][i], data[5][i]]
        tempb = [data[2][i], data[4][i], data[6][i]]
        tTf = np.mean(tempf)
        tTb = np.mean(tempb)
        tTfstd = np.std(tempf,ddof = True)
        tTbstd = np.std(tempb,ddof = True)
        Tf = np.hstack((Tf,tTf))
        Tb = np.hstack((Tb,tTb))
        Tfstd = np.hstack((Tfstd,tTfstd))
        Tbstd = np.hstack((Tbstd,tTbstd))


    slopef, interceptf, r_value, p_value, std_errf = stats.linregress(rh,Tf)
    slopeb, interceptb, r_value, p_value, std_errb = stats.linregress(rh,Tb)

    plt.plot(rh,Tf,"og",label="Periodendauern fest")
    x1,y1=linregfunc(slopef,interceptf)
    plt.plot(x1,y1,"-g",label="LinReg")

    plt.plot(rh,Tb,"ob",label="Periodendauern begewglich")
    x2,y2=linregfunc(slopeb,interceptb)
    plt.plot(x2,y2,"-b",label="LinReg")

    plt.legend()
    plt.title("Periodendauern")
    plt.xlabel("h in cm")
    plt.ylabel("T in s")
    plt.grid(True)
    plt.show()

    slopef = uc.ufloat(slopef,std_errf)
    slopeb = uc.ufloat(slopeb,std_errb)
    interceptf = uc.ufloat(interceptf,0)
    interceptb = uc.ufloat(interceptb,0)
    print(slopef,interceptf)
    lr = (interceptb-interceptf)/(slopef-slopeb)
    print("lr = ",lr)
    Tphy = slopef*lr+interceptf
    print("Tphy = ",Tphy)
    g = value_g(lr,Tphy)
    print("Ortsfaktor = ",g)




















aufgabe12()
