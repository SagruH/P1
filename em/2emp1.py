import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt


def loadCSV(x):
    hlines, data = ppk.readCSV(x,2)
    data = np.array(data)
    U,I=np.split(data,2)
    U = U[0]
    I = I[0]
    return U,I;

def BFeld(I):
    my0 = 1.256637 * 10**(-6)
    L = uc.ufloat(0.2,0.0005)
    n = 3000
    R = uc.ufloat(0.045,0.0005)
    a = 1 # Platzhalter
    B0 = (my0*I*n/L)
    K = (0.567*((a/sqrt(R**2+a**2))+((L-a)/sqrt(R**2+(L-a)**2))))
    B = B0 * K
    return B;

def xyPlatte():
    Ux,Ix = loadCSV("2_2x.csv")
    Uy,Iy = loadCSV("2_2y.csv")

    Ix2 = Ix**2
    Iy2 = Iy**2


    plt.plot(Ux,Ix2, label = "x-Platten")
    plt.plot(Uy,Iy2, label = "y-Platten")
    plt.xlabel("U in V")
    plt.ylabel("I² in A²")
    plt.title("Aufgabe 2 e/m-Bestimmung")
    plt.grid(True)
    plt.legend()
    #plt.show()
    return



#xyPlatte()
