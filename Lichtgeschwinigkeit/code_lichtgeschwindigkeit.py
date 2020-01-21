import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const

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

def aufgabe3():
    '''
    Luft    0,351m
    kurze Seite:
    Wasser  0,365m
    Silikonöl 0,371m
    leerer Behälter 0,335m
    lange Seite:
    Wasser  0,387m
    Silikonöl 0,394m
    leerer Behälter 0,353m
    '''
    L  = 0.351
    Kk = 0.335
    Wk = 0.365
    Sk = 0.371

    Kl = 0.353
    Wl = 0.387
    Sl = 0.394
    dWk = Wk - Kk
    dSk = Sk - Kk
    dWl = Wl - Kl
    dSl = Sl - Kl
    ds = np.array([dWk,dSk,dWl,dSl])
    print("wasser kurz: ", dWk),
    print("Silikon kurz: ", Sk-Kk)
    print("wasser lang: ", Wl-Kl)
    print("Silikon lang: ", Sl-Kl)

    n1 = 1+ (dWk/0.05)
    n2 = 1+ (dSk/0.05)
    n3 = 1+ (dWl/0.1)
    n4 = 1+ (dSl/0.1)
    print(n1,n2,n3,n4)
    return



aufgabe3()
