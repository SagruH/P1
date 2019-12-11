import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt

def loadCSV(name,hlines=2,split=2):
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def aufgabe11():
    '''gemessen 130cm -
        1. 106.2cm
        2. 107.1cm
        3. 105.1cm
        4. 106.0cm
        5. 106.7cm

        f = 20cm real
    '''
    schirm = 130
    p1 = 106.2
    p2 = 107.1
    p3 = 105.1
    p4 = 106.0
    p5 = 106.7
    lp = np.array([p1,p2,p3,p4,p5])
    lf = 130 - lp
    fmean = np.mean(lf)
    fstd = np.std(lf,ddof = True)
    print("Aufgabe 1.1 " ,uc.ufloat(fmean,fstd))
    return;

def evalCSV(name,M):
    big, small = loadCSV(name)
    if M == 1:
        dia = 45
    elif M == 2:
        dia = 35
    else:
        print("error: invalid M")

    a1 = big - dia
    a2 = small - dia
    a1mean = np.mean(a1)
    a1std = np.std(a1,ddof = True)
    a2mean = np.mean(a2)
    a2std = np.std(a2,ddof = True)
    return a1mean, a1std, a2mean, a2std;

def f_and_error(data,e):
    fafer = [0,1,2,3]
    eabw = 0.01
    for i in [0,1,2,3]:
        a1 = data[i][0]
        a1std = data[i][1]
        a2 = data[i][2]
        a2std = data[i][3]

        # need e a1std a2std a1 a2
        f = (e**2 - (a2 - a1)**2)/(4*e)
        a1er = (((a2-a1)*a1std)/(2*e))**2
        a2er = (((a2-a1)*a2std)/(2*e))**2
        eer = (((e**2+(a2-a1)**2)*eabw)/(4*e**2))**2
        fer = np.sqrt(a1er + a2er + eer)
        fafer[i] = [f,fer]
    return fafer;


def foveruc(data,e):
    fuc = np.array([])
    for i in [0,1,2,3]:
        a1 = uc.ufloat(data[i][0],data[i][1])
        a2 = uc.ufloat(data[i][2],data[i][3])
        ex  = uc.ufloat(e,0.01)
        f = (ex**2 - (a2 - a1)**2)/(4*ex)
        fuc = np.hstack((fuc,f))
    return fuc;


def aufgabe12():
    schirm = 130
    farbe = 29
    dia1 = 45
    dia2 = 35
    e1 = schirm - dia1
    e2 = schirm - dia2
    data_list_M1 = np.array(["12ba1.csv","12bi1.csv","12ra1.csv","12ri1.csv"])
    data_list_M2 = np.array(["12ba2.csv","12bi2.csv","12ra2.csv","12ri2.csv"])

    meanandstd_M1 = [0,1,2,3]
    meanandstd_M2 = [0,1,2,3]
    j = 0
    for s in data_list_M1:
        s = str(s)
        a1mean, a1std, a2mean, a2std = evalCSV(s,1)
        meanandstd_M1[j] = [a1mean, a1std, a2mean, a2std]
        j += 1
        #print(s," a1: ",uc.ufloat(a1mean,a1std)," a2: ",uc.ufloat(a2mean,a2std))

    j = 0
    for s in data_list_M2:
        s = str(s)
        a1mean, a1std, a2mean, a2std = evalCSV(s,2)
        meanandstd_M2[j] = [a1mean, a1std, a2mean, a2std]
        j += 1
        #print(s," a1: ",uc.ufloat(a1mean,a1std)," a2: ",uc.ufloat(a2mean,a2std))

    f1 = f_and_error(meanandstd_M1,e1)
    f2 = f_and_error(meanandstd_M2,e2)
    fuc1 = foveruc(meanandstd_M1,e1)
    fuc2 = foveruc(meanandstd_M2,e2)

    fuca = np.hstack((fuc1,fuc2))
    ff = np.mean(fuca)
    print("Aufgabe 1.2 " ,ff)
    return;

aufgabe11()
aufgabe12()
