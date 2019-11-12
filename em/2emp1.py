import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc

def loadCSV(x):
    hlines, data = ppk.readCSV(x,2)
    data = np.array(data)
    U,I=np.split(data,2)
    U = U[0]
    I = I[0]
    return U,I;

def xPlatte():
    Ux,Ix = loadCSV("2_2x.csv")
    print(Ux,Ix)
    return

def yPlatte():
    Uy,Iy = loadCSV("2_2y.csv")
    print(Uy,Iy)
    return

yPlatte()
xPlatte()
