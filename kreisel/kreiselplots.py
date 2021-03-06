import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par


def loadCSV(x):
    hlines, data = ppk.readCSV(x,1)
    data = np.array(data)
    t,v=np.split(data,2)
    t = t[0]
    v = v[0]
    return t,v;

def linregfunc(m,b):
    x=np.linspace(4,26,1000)
    f = m*x+b
    return f,x;

def nutplot():
    KoG, NoG = loadCSV("3_0ohneGewichtedata.csv")
    KmG, NmG = loadCSV("3_1mitGewichtedata.csv")

    xslopeoG, interceptoG, xr_value, p_value, xstd_err = stats.linregress(KoG,NoG)
    fxoG, xxoG = linregfunc(xslopeoG,interceptoG)

    xslopemG, interceptmG, xr_value, p_value, xstd_err = stats.linregress(KmG,NmG)
    fxmG, xxmG = linregfunc(xslopemG,interceptmG)
    #melanie
    print("Steigung mit gewichte der Reg Gerade: " , xslopemG, "Steigung ohne Gewichte:" , xslopeoG)

    plt.plot(xxoG,fxoG, label = "Regressionsgerade ohne Gewichte")
    plt.plot(KoG,NoG ,"og" , label = "Messung ohne Gewichte")

    plt.plot(xxmG,fxmG, label = "Regressionsgerade mit Gewichte")
    plt.plot(KmG,NmG ,"or" , label = "Messung mit Gewichten",)

    plt.ylabel("Nutationsfrequenz in Hz")
    plt.xlabel("Kreiselfrequenz in Hz")
    plt.title("Aufgabe 3 Nutation")
    plt.grid(True)
    plt.legend()
    plt.show()

    return;


def praezplot():
    Kf, pT = loadCSV("5praedata.csv")

    pf = np.array([])
    for i in pT:
        x = 1/i
        pf = np.hstack((pf,x))

    xslopeoG, interceptoG, xr_value, p_value, xstd_err = stats.linregress(Kf,pT)
    fx, xx = linregfunc(xslopeoG,interceptoG)

    plt.plot(xx,fx , label = "Regressionsgerade")
    plt.plot(Kf,pT ,"or" , label = "Messwerte",)

    plt.ylabel("Präzessionszeit in s")
    plt.xlabel("Kreiselfrequenz in Hz")
    plt.title("Aufgabe 5 Präzessions")
    plt.grid(True)
    plt.legend()
    plt.show()

    return;



nutplot()
