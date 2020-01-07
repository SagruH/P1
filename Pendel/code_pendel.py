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

def calibrate(): #berechung des offsets
    n,t = loadCSV("1_1data.csv")
    slope, intercept, r_value, p_value, std_err = stats.linregress(n,t)
    #print(slope, intercept, r_value, p_value, std_err)
    #plt.plot(n,t)
    #plt.plot(n,t,'og')
    #plt.show()
    print("Offset: ", intercept)
    return intercept;

def aufgabe12():
    rh,rM1f,rM1b,rM2f,rM2b,rM3f,rM3b,data= load_huge_CSV("1_2data.csv")
    offset = calibrate()
    data[1:] = data[1:]/1000 # time from ms to s
    data[1:] = data[1:]-offset # offset korrektur
    print(data)
    '''
    for x in np.arange(1,7):
        plt.plot(data[0],data[x],label=str(x))
        plt.legend()
    plt.show()
    '''

























aufgabe12()
