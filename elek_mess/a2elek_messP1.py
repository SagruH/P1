import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt


def loadCSV(name,hlines=1,split=2):
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b,c=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    c = c[0]
    return a,b,c;

#aufgabe 2

#aufgabe 2.2

def RLundL():
    UG = 0.2 #V
    UR = 0.08 #V
    UL = 0.15 #V
    RR = 110 #Ohm
    f = 30 #Hz
    w = 2*np.pi*f

    RL = ((UG**2-UL**2-UR**2)/(2*UR**2))*RR
    L = (RR/(UR*w))*np.sqrt(UL**2-UR**2)

    print("Aufgabe 2:\nVerlustwiderstand der Spule: ", RL ,"\nInduktivität L: ", L)
    return;
















RLundL()
