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

def linregfunc1(m,b):
    x=np.linspace(500,3000,100)
    f = m*x+b
    return x,f;

def aufgabe12_plots():
    U = np.linspace(600,2700,8)
    v = np.array([4,4.8,5.5,6.4,7.8,8.7,9.8,10.9])

    slope, intercept, r_value, p_value, std_err = stats.linregress(U,v)

    x,f = linregfunc1(slope,intercept)

    plt.plot(U,v, "-b")
    plt.plot(U,v, "ob")
    plt.plot(x,f)

    plt.ylabel("Luftgeschwindigkeit in m/s")
    plt.xlabel("Umdrehungen pro Minute")
    plt.title("Luftgeschwindigkeit bei r=0cm und l=20cm")
    plt.grid(True)
    plt.legend()
    plt.show()
    return;

def linregfunc2(m,b):
    x=np.linspace(3.5,11.5,100)
    f = m*x+b
    return x,f;

def aufgabe21u2():
    dK1 = 4 #cm durchmesser der Scheiben
    dK2 = 5.6
    dK3 = 8
    dK = np.array([dK1,dK2,dK3])
    rK = dK/2
    AK = rK**2 * np.pi
    l= 20

    print("Fläsche Kreisscheibe 1-3 in cm²: " , AK)

    FK1 = 0.8 #N Kraft auf Scheiben
    FK2 = 2.1
    FK3 = 3.9
    FK = np.array([FK1,FK2,FK3])
    FproA = FK/AK
    print("Druck pro Fläche auf Kreisscheiben: " , FproA)

    #Aufagbe 2.2
    U = np.linspace(600,2700,8)
    v = np.array([4,4.8,5.5,6.4,7.8,8.7,9.8,10.9])

    K2F2 = np.array([0,0.1,0.4,0.7,0.9,1.2,1.6,2])
    K3F2 = np.array([0.4,0.5,0.7,1.2,1.7,2.6,3.2,4.1])


    slope, intercept, r_value, p_value, std_err = stats.linregress(v,K2F2)
    x,f = linregfunc2(slope,intercept)
    plt.plot(x,f,"-b") #linreg
    plt.plot(v,K2F2,"-b", label = "mittlere Kreisscheibe")
    plt.plot(v,K2F2,"ob")

    slope, intercept, r_value, p_value, std_err = stats.linregress(v,K3F2)
    x,f = linregfunc2(slope,intercept)
    plt.plot(x,f,"-g") #linreg
    plt.plot(v,K3F2,"-g", label = "große Kreisscheibe")
    plt.plot(v,K3F2,"og")

    plt.xlabel("Windgeschwindigkeit in m/s")
    plt.ylabel("Kraft in N")
    plt.title("Aufgabe 2.2: Stömungswiderstand über Windgeschwindigkeit")
    plt.grid(True)
    plt.legend()
    plt.show()

    return;


def aufgabe23u4():
    U = 2700
    v = 10.9 #m/s

    d = 0.056 #m
    A = (d/2)**2 * np.pi
    p = 1.2

    #HK konvex ; HK flach ; Kugel ; StromlK
    F_array = np.array([1.1,3.2,0.8,0.2])

    cw = (2*F_array*0.1)/(p*A*v**2)


    print("Querschnittfläche :" , A)
    print("cw Werte: " , cw)

    #Aufgabe2.4
    AS = 0.015*0.005 #m
    FS = 0.4
    cwS = (2*FS*0.1)/(p*AS*v**2)

    print("A Spielzeug: " , AS)
    print("cw Spielzeug: " , cwS)

    return;








aufgabe23u4()
