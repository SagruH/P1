import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par
#Aufgabe 5.1
#-------------------------------------------------------------
def loadCSV():
    hlines, data = ppk.readCSV("signal.csv")
    data = np.array(data)
    t,a=np.split(data,2)
    t = t[0]
    a = a[0]
    return t,a;

def C51a():
    #Teil a
    
    t,a=loadCSV()
    plt.plot(t,a)
    
    plt.title("Aufgabe 5.1 a")
    plt.xlabel("Zeit in ms")
    plt.ylabel("Amplitude in V")
    plt.show()

def C51b():
    #Teil b
    
    t,a=loadCSV()
    ag=ppk.meanFilter(a,15)
    diff = ag-a
    
    #geglättet
    
    plt.plot(t,ag)
    plt.title("Aufgabe 5.1 b geglättet")
    plt.xlabel("Zeit in ms")
    plt.ylabel("Amplitude in V")
    plt.show()

    #differenz

    plt.plot(t,diff)
    plt.title("Aufgabe 5.1 b differenz")
    plt.xlabel("Zeit in ms")
    plt.ylabel("Amplitude in V")
    plt.show()

def minmaxfind(a): #findet Hoch/Tief Punkte (Aufgabe 5.1 c)
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

def C51c():
    #Teil c
    t,a=loadCSV()
    ag=ppk.meanFilter(a,15)
    acor = ppk.autocorrelate(ag)
    
    plt.plot(t,acor)
    plt.title("Aufgabe 5.1 c autocorr")
    plt.xlabel("Zeit in ms")
    plt.ylabel("Amplitude in V")
    plt.grid(1)
    plt.show()
    plt.clf()
    #maxpos = ppk.convolutionPeakfinder(acor)
    HP,TP = minmaxfind(acor) #bessere Version von Zeile drüber
    #print("Hochpunkte ",t[HP],"Tiefpunkte ",t[TP])

    #differenz min & max
    HPdiff = np.array([])
    TPdiff = np.array([])
    for x in np.arange(len(HP)-1):
        Hdiff = t[x+1]-t[x]
        HPdiff = np.hstack((HPdiff,Hdiff))
    for y in np.arange(len(TP)-1):
        Tdiff = t[y+1]-t[y]
        TPdiff = np.hstack((TPdiff,Tdiff))

    #histogrammme
    plt.hist((TPdiff,HPdiff),bins=np.arange(0.,0.1,0.01))
    plt.title("Aufgabe 5.1 c Histogramm diff")
    plt.show()
    print("daraus folgt eine Periode von ",round(np.sum(HPdiff)/len(HPdiff),6),"ms")
    return;

#Aufgabe 5.2
#-------------------------------------------------------------
def C52():
    #Erster Teil von Aufgabe 5.2a
    N1 = 100
    dataN1 = np.random.rand(N1)
    bins1 = np.linspace(0,1,6)
    hist1 ,trash = np.histogram(dataN1,bins=bins1)
    print("Das Histogramm für N = 100 mit 5 bins ist:",hist1)
    print("Erwartet wird: ", int(N1/5) ,"pro bin.\n")

    #Zweiter Teil von Aufgabe 5.2a
    nexp = 10000
    bins2 = np.linspace(0,1,6)
    n = dict() 
    for p in range(1,6):
        n[p] = np.array([])
    i = 0
    while i < nexp:
        i +=1
        dataN1 = np.random.rand(N1)
        hist1 ,bined = np.histogram(dataN1,bins=bins1)
        for k in range(1,6):
            n[k] = np.hstack((n[k],hist1[k-1]))
            
    #Histogramm für Aufgabe 5.2a  
    print("Ich erwarte am meisten Werte um 20\n")
    plt.hist((n[1],n[2]))
    plt.title("Aufgabe 5.2a Histogramm für n1 & n2")
    plt.show()

    
    #2D Histogramm für Aufgabe 5.2b
    plt.clf()
    hist, xedge, yedge, trash = plt.hist2d(n[1],n[2])
    meanx,meany,varx,vary,cov,cor = ppk.hist2dstat(hist, xedge, yedge)
    print("Der Korrelationskoeffizient ist:" , round(cor,4))
    plt.title("Aufgabe 5.2b 2d-Histogramm")
    plt.show()
    return;

#Aufgabe 5.3
#-------------------------------------------------------------
def aline(x,a,b): #funktion zu a
    return a*x+b

def bline(x,c): #funktion zu b
    return 1 * (x-15) + c
def C53a():
    #Aufgaben Teil a
    xm, ym = np.loadtxt("FittingExercise.dat", unpack=True)
    kdata = kafe.Dataset(data=(xm,ym))
    kdata.add_error_source('y', 'simple', 1.0)
    fitf = aline
    kfit= kafe.Fit(kdata,fitf)
    kfit.do_fit()
    kplot = kafe.Plot(kfit)
    kplot.axis_labels = ['x', 'Daten und  f(x)']
    kplot.plot_all()
    kfit.plot_correlations()
    kplot.show()
    return

def C53b():
    #Aufgaben Teil b
    xm, ym = np.loadtxt("FittingExercise.dat", unpack=True)
    kdata = kafe.Dataset(data=(xm,ym), title="Fitting Exercise data")
    kdata.add_error_source('y', 'simple', 1.0)
    fitf = bline
    kfit= kafe.Fit(kdata,fitf)
    kfit.do_fit()
    kplot = kafe.Plot(kfit)
    kplot.axis_labels = ['x', 'Daten und  f(x)']
    kplot.plot_all()
    kfit.plot_correlations() #führt zu fehler keine Ahnung wieso
    kplot.show()
    return

                              
#um Aufgabe hier auszuführen: entkommentieren
#C51a()
#C51b()
#C51c()
#C52()
#C53a()
#C53b()
