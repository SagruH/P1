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
    print(fmean,fstd)
    return;

def evalCSV(name):
    a, b = loadCSV(name)


    return mean, std;


def aufgabe12():
    data_list_blue= np.array(["12ba1.csv","12ba2.csv","12bi1.csv","12bi2.csv"])
    data_list_red = np.array(["12ra1.csv","12ra2.csv","12ri1.csv","12ri2.csv"])

    return;
