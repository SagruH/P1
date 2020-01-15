import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats

#import kafe
#from kafe.function_tools import FitFunction, LaTeX, ASCII
#from kafe.function_library import quadratic_3par

#import uncertainties as uc
#from uncertainties.umath import sqrt

def loadCSV(name,hlines=1,split=2):
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def linregfunc(m,b):
    x=np.linspace(0.0185,0.0215,100)
    f = m*x+b
    return x,f;

def aufgabe1():
    f,s = loadCSV("1daten.csv")
    d = 6.579
    d1 = 7.23
    d2 = 6.57
    f = f / 60 #f in Hz
    s = s / 1000

    ds = np.array([0])
    for i in np.arange(1,len(s)):
        ss = s[i]-s[0]
        ds = np.hstack((ds,ss))


    lamda = 8*np.pi*d*(d1+d2)
    lf = lamda*f

    slope, intercept, r_value, p_value, std_err = stats.linregress(s,lf)
    x,f = linregfunc(slope,intercept)
    #y=mx ; lf=c*s
    print(slope/1000000,std_err/1000000)
    '''
    plt.plot(s,lf,'og')
    plt.plot(x,f,'-b')
    plt.title("Aufgabe 1: Daten")
    plt.xlabel("s")
    plt.ylabel("λf")
    plt.grid(True)
    plt.show()
    '''
    return;


aufgabe1()
