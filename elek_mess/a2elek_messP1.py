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

#aufgabe 2.3
def aufgabe23u4():
    f, U, dt = loadCSV("2_3data.csv",1,3)
    dphi = 2*np.pi*f*dt/1000
    w = 2*np.pi*f
    f0 = 198.8
    w0 = 2*np.pi*f0

    #find delta
    #print(np.max(U)/2.) =71.2
    Dwpos1 = np.where(U == 68.2)
    Dwpos2 = np.where(U == 67)
    Dw = w[Dwpos2]-w[Dwpos1]

    #plot f-U
    plt.xlabel("Frequenz in Hz")
    plt.ylabel("Spannung in mV")
    plt.plot(f,U,"or")
    plt.plot(f,U,"b")
    plt.grid(True)
    #plt.show()
    plt.clf()


    #plot dphi-f
    plt.xlabel("Frequenz in Hz")
    plt.ylabel("Phasenverschiebung in Grad")
    plt.plot(f,dphi,"or")
    plt.plot(f,dphi,"b")
    plt.grid(True)
    #plt.show()
    plt.clf()

    #weitere Brechnungen
    UR = np.max(U)/1000
    U0 = 9.2
    RV = 10**6
    RR = UR * RV/(U0-UR)

    C = np.sqrt(3)/(RR*Dw)
    L = 1/(w0**2*C)
    R = (Dw*L)/np.sqrt(3)

    #Aufgabe 2.4

    LI = 6.06/1000 #A
    LU = 7.9 #V AC
    C2I = 6.28/1000 # A
    C2U = LU

    RL = LU/LI
    RC = C2U/C2I

    C4 = 1/(RC*w0)
    L4 = RL/w0

    print(C4,L4)

    return;

def aufgabe24():
    LI = 6.06/1000 #A
    LU = 7.9 #V AC
    C2I = 6.28/1000 # A
    C2U = LU

    RL = LU/LI
    RC = C2U/C2I


    print(RC,RL)
    return;












aufgabe23u4()
