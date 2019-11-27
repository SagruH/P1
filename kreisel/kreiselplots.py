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
    x=np.linspace(1,18,1000)
    f = m*x+b
    return f,x;

def nutplot():
    KoG, NoG = loadCSV("3_0ohneGewichtedata.csv")
    KmG, NmG = loadCSV("3_1mitGewichtedata.csv")

    #xslopeoG, interceptoG, xr_value, p_value, xstd_err = stats.linregress(KoG,NoG)
    #fxoG, xxoG = linregfunc(xslopeoG,interceptoG)

    xslopemG, interceptmG, xr_value, p_value, xstd_err = stats.linregress(KmG,KmG)
    fxmG, xxmG = linregfunc(xslopemG,interceptmG)

    #plt.plot(xxoG,fxoG, label = "Regressionsgerade ohne Gewichte")
    #plt.plot(KoG,NoG ,"og" , label = "Messung ohne Gewichte")

    plt.plot(xxmG,fxmG, label = "Regressionsgerade mit Gewichte")
    plt.plot(KmG,NmG ,"or" , label = "Messung mit Gewichten",)

    plt.ylabel("Nutationsfrequenz in Hz")
    plt.xlabel("Kreiselfrequenz in Hz")
    plt.title("Aufgabe 3 Nutation")
    plt.grid(True)
    plt.legend()
    plt.show()

    return;

nutplot()
