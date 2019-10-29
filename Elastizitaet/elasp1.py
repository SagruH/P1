import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc

def loadCSV(x):
    hlines, data = ppk.readCSV(x,3)
    data = np.array(data)
    t,v=np.split(data,2)
    t = t[0]
    v = v[0]
    return t,v;


def minmaxfind(a):
    HP = np.array([])
    TP = np.array([])
    l = len(a)
    j = a[0]
    HPisNext = 1
    for k in np.arange(1,l):
        i=a[k]
        if HPisNext == 1:
            if j>i:
                HP = np.hstack((HP,k-1))
                HPisNext=0
        elif HPisNext == 0:
            if j<i:
                TP = np.hstack((TP,k-1))
                HPisNext=1
        j=a[k]
    HP=np.int_(HP)
    TP=np.int_(TP)
    return HP,TP;

def Xpeak(t,v,th):
    HP,TP = minmaxfind(v)
    j = 0
    peak = np.array([])
    for i in HP:
        if v[i] > th:
            peak = np.hstack((peak,t[i]))
        j+=1
    return peak;


def Alu():
    print("-----Alu-----")
    t,v = loadCSV("Alu.csv")
    vcor = ppk.autocorrelate(v)
    th = 1.5e-01
    peak = Xpeak(t,vcor,th)

    peakdiff = np.array([])
    for x in np.arange(len(peak)):
        if x >= 1:
            y = peak[x] - peak[x-1]
            peakdiff = np.hstack((peakdiff,y))

    print("Differenzen der peaks in ms", peakdiff)
    pmean = np.mean(peakdiff)
    per = np.std(peakdiff)/np.sqrt(len(peakdiff))

    pt = uc.ufloat(pmean,per) # in ms
    print("mean is ", pt)
    lm = 0.525 + 0.013
    ler = 0.0005
    l = uc.ufloat(lm,ler) #länge stab m
    rho = 2710 #dichte alu kg/m³

    vel = 2*l/(pt/1000)

    print("Ausbreitungsgeschwindigkeit ist",vel)

    E = vel**2 * rho
    print("Das E Modul ist", E)
    plt.plot(t,v)
    plt.title("Alu")
    plt.grid(True)
    #plt.plot(t,vcor)
    plt.show()
    return;

def Kupfer(): #zwei werte gelöscht da v = infinty
    print("-----Kupfer-----")
    t,v = loadCSV("Kupfer.csv")
    #vcor = ppk.autocorrelate(v)
    th = 60
    peak = Xpeak(t,v,th)

    peakdiff = np.array([])
    for x in np.arange(len(peak)):
        if x >= 1:
            y = peak[x] - peak[x-1]
            peakdiff = np.hstack((peakdiff,y))

    pmean = np.mean(peakdiff)
    per = np.std(peakdiff)/np.sqrt(len(peakdiff))

    pt = uc.ufloat(pmean,per) # in ms
    print("Differenzen der peaks in ms", peakdiff)
    print("mean is ", pt)

    lm = 0.525 + 0.013
    ler = 0.0005
    l = uc.ufloat(lm,ler) #länge stab m
    rho = 8920 #dichte Kupfer kg/m³

    vel = 2*l/(pt/1000)
    E = vel**2 * rho
    print("Ausbreitungsgeschwindigkeit ist", vel)
    print("Das E Modul ist", E)

    plt.plot(t,v)
    plt.title("Kupfer")
    plt.grid(True)
    #plt.plot(t,vcor)
    plt.show()
    return;

def PVC():
    print("-----PVC-----")
    t,v = loadCSV("PVC1.csv")
    th = 200
    peak = Xpeak(t,v,th)

    peakdiff1 = np.array([])
    for x in np.arange(len(peak)):
        if x >= 1:
            y = peak[x] - peak[x-1]
            peakdiff1 = np.hstack((peakdiff1,y))

    t2,v2 = loadCSV("PVC2.csv")
    th2 = 400
    peak2 = Xpeak(t,v,th)

    peakdiff2 = np.array([])
    for x in np.arange(len(peak2)):
        if x >= 1:
            y = peak2[x] - peak2[x-1]
            peakdiff2 = np.hstack((peakdiff2,y))


    peakdiff = np.hstack((peakdiff1,peakdiff2))
    pmean = np.mean(peakdiff)
    per = np.std(peakdiff)/np.sqrt(len(peakdiff))

    pt = uc.ufloat(pmean,per) # in ms
    print("Differenzen der peaks in ms", peakdiff)
    print("mean is ", pt)

    lm = 0.525 + 0.013
    ler = 0.0005
    l = uc.ufloat(lm,ler) #länge stab m
    rho = 1400 #dichte PVC kg/m³

    vel = 2*l/(pt/1000)
    E = vel**2 * rho
    print("Ausbreitungsgeschwindigkeit ist", vel)
    print("Das E Modul ist", E)

    plt.plot(t,v)
    plt.plot(t2,v2)
    plt.title("PVC")
    plt.grid(True)
    #plt.plot(t,vcor)
    plt.show()
    return;

def Messing():
    print("-----Messing-----")
    t,v = loadCSV("Messing.csv")
    vcor = ppk.autocorrelate(v)

    th = 0.75
    peak = Xpeak(t,v,th)

    peakdiff = np.array([])
    for x in np.arange(len(peak)):
        if x >= 1:
            y = peak[x] - peak[x-1]
            peakdiff = np.hstack((peakdiff,y))

    pmean = np.mean(peakdiff)
    per = np.std(peakdiff)/np.sqrt(len(peakdiff))

    pt = uc.ufloat(pmean,per) # in ms
    print("Differenzen der peaks in ms", peakdiff)
    print("mean is ", pt)

    lm = 0.525 + 0.013
    ler = 0.0005
    l = uc.ufloat(lm,ler) #länge stab m
    rho = 8730 #dichte Messing kg/m³

    vel = 2*l/(pt/1000)
    E = vel**2 * rho
    print("Ausbreitungsgeschwindigkeit ist", vel)
    print("Das E Modul ist", E)

    plt.plot(t,v)
    plt.title("Messing")
    plt.grid(True)
    #plt.plot(t,vcor)
    plt.show()
    return;
Kupfer()
Alu()
PVC()
Messing()
