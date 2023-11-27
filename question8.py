import numpy as np
import math
nmk = input("").split(" ")
n = int(nmk[0])
m = int(nmk[1])
kinp = int(nmk[2])

X = []
Y = []
for i in range(n):
    row = input("").split(" ")
    a = []
    for j in row:
        a.append(int(j))
    X.append(a)

Y = input("").split(" ")
for i in range(len(X)):
    for j in range(len(X[i])):
        X[i][j] = int(X[i][j])

for i in range(len(Y)):
    Y[i] = int(Y[i])
Parray = []
for i in range(m):
    Parray.append([])

for i in range(m):
    uniques = []
    for j in range(n):
        if(X[j][i] not in uniques):
            uniques.append(X[j][i])
    maxa = max(uniques)
    for k in range(maxa+1):
        Parray[i].append(0)


for i in range(len(Parray)):
    for j in range(n):
        Parray[i][X[j][i]] += 1

for i in range(len(Parray)):
    for j in range(len(Parray[i])):
        Parray[i][j] = Parray[i][j]/n
        
Hx = []
for i in range(m):
    h = 0
    for j in range(len(Parray[i])):
        h += (-1) * Parray[i][j] * math.log(Parray[i][j], 2)
    Hx.append(h)


Py = [0,0]
for i in range(len(Y)):
    Py[Y[i]] += 1
Py[0] = Py[0]/n
Py[1] = Py[1]/n

Pxy = Parray
for i in range(len(Pxy)):
    for j in range(len(Pxy[i])):
        tup = [0,0]
        Pxy[i][j] = tup

for i in range(len(Pxy)):
    for j in range(n):
        Pxy[i][X[j][i]][Y[j]] += 1

for i in range(len(Pxy)):
    for j in range(len(Pxy[i])):
        for k in range(len(Pxy[i][j])):
            Pxy[i][j][k] = Pxy[i][j][k]/n

Ixyarr = []
for i in range(m):
    Ixy = 0
    Hxy = 0
    for j in range(len(Pxy[i])):
        if(Pxy[i][j][0] != 0):
            Hxy += Pxy[i][j][0]*math.log(1/Pxy[i][j][0], 2)
        if(Pxy[i][j][1] != 0):  
            Hxy += Pxy[i][j][1]*math.log(1/Pxy[i][j][1], 2)
    Ixy = Hx[i] + ((-1)*(Py[0]*math.log(Py[0], 2) + (Py[1]*math.log(Py[1], 2)))) - Hxy
    Ixyarr.append(Ixy)

inds = np.argsort(Ixyarr)[::-1]
for i in range(kinp):
    print(inds[i]+1, end=" ")
