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
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def aufgabe11_plots():
    #offset 5PA
    offset = 5
    #2600U/min
    l = np.array([8,18,28,33]) #in cm
    r,p_off = loadCSV("aufgabe11.csv") #r in c , p in Pa
    p = p_off - offset
    parray = [0,1,2,3]
    k = -1
    for i in np.arange(0,len(r)):   #sortiert druck zu laengen in 4 arrays
        if r[i] == 0:
            j=i
            k += 1
            parray[k] = [p[j:j+6]]
        #print(i,j,k)
    #print(parray)

    #plots :
    r = np.array([0,1,2,3,4,5])

    plt.plot(r,parray[0][0], "-g", label = "Abstand 8cm")
    plt.plot(r,parray[0][0], "og")

    plt.plot(r,parray[1][0],"-r", label = "Abstand 18cm")
    plt.plot(r,parray[1][0] ,"or")

    plt.plot(r,parray[2][0],"-b" , label = "Abstand 28cm")
    plt.plot(r,parray[2][0],"ob")

    plt.plot(r,parray[3][0],"-y", label = "Abstand 33cm")
    plt.plot(r,parray[3][0],"oy")

    plt.ylabel("Druck in Pa")
    plt.xlabel("Abstand vom Mittelpunkt: r in cm")
    plt.title("Aufgabe 1.1: Staudruck im Luftstrom")
    plt.grid(True)
    plt.legend()
    plt.show()


    return;

aufgabe11_plots()
