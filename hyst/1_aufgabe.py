import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt


def loadCSV(x):
    hlines, data = ppk.readCSV(x,3)
    data = np.array(data)
    t,V1,V2=np.split(data,3)
    t = t[0]
    V1 = V1[0]
    V2 = V2[0]
    return t,V1,V2;

def main():
    t, V1, V2 = loadCSV("1_1Messung_32.csv")
    plt.plot(t,V1, label="Widerstand")
    plt.plot(t,V2, label="Spule")
    plt.grid(True)
    plt.legend()
    plt.show()
    return;

def HB_plot():
    t, V1, V2 = loadCSV("3_1Messung.csv")
    V1 = V1*208.33/1000
    V2 = V2*1.32/1000
    plt.xlabel("H-Feld")
    plt.ylabel("B-Feld")
    plt.plot(V1,V2)
    plt.grid(True)
    plt.title("H-B Kurve")
    plt.show()
    return;

HB_plot()
