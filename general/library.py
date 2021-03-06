def loadCSV(name,hlines=1,split=2):
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

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


def num_int_calc(d, S): #needs test
    a = np.linspace(d,S,10000)
    da = a[100]-a[99]
    lamda = np.array([])
    Integral= 0
    for i in a:
        y = lamdafunc(i) #name der funktion unter der integriert wird
        lamda = np.hstack((lamda,y))

    for j in np.arange(len(lamda)):
        if j>0:
            Integral = Integral + (lamda[j-1]*da) + (lamda[j]-lamda[j-1])*da*1/2

    lamdaq = (1/(S-d))*Integral
    return lamdaq;
