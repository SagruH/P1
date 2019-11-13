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
    hlines, data = ppk.readCSV(x,2)
    data = np.array(data)
    U,I=np.split(data,2)
    U = U[0]
    I = I[0]
    return U,I;



def lamdafunc(a):
    my0 = 1.256637 * 10**(-6)
    L = uc.ufloat(0.2,0.0005)
    n = 3000
    R = uc.ufloat(0.045,0.0005)
    K = (0.567*((a/sqrt(R**2+a**2))+((L-a)/sqrt(R**2+(L-a)**2))))
    lamda = (my0 * n/L)*K
    return lamda;

def lamdaqcalc(d, S):
    a = np.linspace(d,S,10000)
    ad = a[100]-a[99]
    lamda = np.array([])
    Integral= 0
    for i in a:
        y = lamdafunc(i)
        lamda = np.hstack((lamda,y))

    for j in np.arange(len(lamda)):
        if j>0:
            Integral = Integral + (lamda[j-1]*ad) + (lamda[j]-lamda[j-1])*ad*1/2

    lamdaq = (1/(S-d))*Integral
    return lamdaq;

def plotlamda():
    a = np.linspace(-0.5,0.5,1000)
    lamda = np.array([])
    for i in a:
        y = lamdafunc(i)
        y = y.n
        lamda = np.hstack((lamda,y))
    print(lamda)
    plt.plot(a,lamda)
    plt.grid(True)
    plt.show()
    return;


def linregfunc(m,b):
    x=np.linspace(0,0.19,1000)
    f = m*x+b
    return f,x;

def xyPlatte():
    Ux,Ix = loadCSV("2_2x.csv")
    Uy,Iy = loadCSV("2_2y.csv")

    Ix2 = Ix**2
    Iy2 = Iy**2

    d2 = uc.ufloat(0.062,0.001) # ist d1 beschreibt dy
    d1 = uc.ufloat(0.08,0.001) #ist d2 beschreibt dx
    S = uc.ufloat(0.15,0.001)

    lamdaq1 = lamdaqcalc(d1,S)
    lamdaq2 = lamdaqcalc(d2,S)

    vfx = (8*(np.pi**2))/(d1**2 * lamdaq1**2)
    vfy = (8*(np.pi**2))/(d2**2 * lamdaq2**2)

    xslope, intercept, xr_value, p_value, xstd_err = stats.linregress(Ix2,Ux)
    fx, xx = linregfunc(xslope,intercept)

    yslope, intercept, yr_value, p_value, ystd_err = stats.linregress(Iy2,Uy)
    fy, xy = linregfunc(yslope,intercept)

    print("r auf x: " , xr_value , "r auf y: " , yr_value)
    print("m von x: " , xslope , "m von y: " , yslope)

    mx = uc.ufloat(xslope, xstd_err)
    my = uc.ufloat(yslope, ystd_err)

    edmx = mx * vfx
    edmy = my * vfy
    print("e/m auf x ist: " , edmx , "e/m auf y ist: " , edmy)

    plt.plot(xx,fx, label = "x-Regressionsgerade")
    plt.plot(Ix2,Ux ,"og" , label = "x-Messungen",)

    plt.plot(xy,fy, label = "y-Regressionsgerade")
    plt.plot(Iy2,Uy, "or" , label = "y-Messungen")

    plt.ylabel("U in V")
    plt.xlabel("I² in A²")
    plt.title("Aufgabe 2 e/m-Bestimmung")
    plt.grid(True)
    plt.legend()
    plt.show()

    return

xyPlatte()
