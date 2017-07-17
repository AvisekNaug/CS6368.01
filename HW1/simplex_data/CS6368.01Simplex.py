import numpy as np
import math
with open('A.txt','r') as f:
    AList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            AList.append(line)
with open('b.txt','r') as f:
    bList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            bList.append(line)
with open('c.txt','r') as f:
    cList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            cList.append(line)
Aprime = np.matrix(AList)
b = np.matrix(bList)
#print b
cprime = np.matrix(cList)
m,nprime = Aprime.shape
n=m+nprime
A=np.concatenate((Aprime,np.matrix(np.identity(m,dtype=float))),axis=1)
c=np.concatenate((cprime,np.matrix(np.zeros((m,1),dtype=float))),axis=0)
#Initializing:
#Basis
Q = [0]*nprime + [1]*m
B = np.matrix(np.identity(m,dtype=float))
Temp1 = B.getI()*b
Xbfs = []
j1 = 0
for i1 in range(n):
    if Q[i1]==1: Xbfs.append(Temp1.item(j1,0)); j1+= 1
    else: Xbfs.append(0)
while True:
    #CreatingCb
    Cb = []
    for i2 in range(n):
        if Q[i2]==1: Cb.append(c.item(i2,0))
    Cb = np.matrix(Cb) # Here Cb is a row matrix. To formulate according to problem use reshape command
    for i3 in range(n):
        c[i3][0] = c[i3][0] - Cb*B.getI()*A[:,i3]
    Optimal = True
    for i4 in range(n):
        if Q[i4]==0 and c[i4][0]<0: Optimal = False; break
    if Optimal == True: break
    TempdB = -B.getI()*A[:,i4]
    d = []
    j5 = 0
    for i5 in range(n):
        if Q[i5]==0 and i5!=i4: d.append(0)
        elif Q[i5]==0 and i5==i4: d.append(1)
        else: d.append(TempdB.item(j5,0)); j5 += 1
    temp = []
    for i6 in range(n):
        if d[i6] < 0: temp.append(-Xbfs[i6]/d[i6])
        else: temp.append(float("inf"))
    theta = min(temp)
    idx = temp.index(theta)
    #Update
    Q[idx] = 0
    Q[i4] = 1
    basicColumns = []
    for i7 in range(n):
        if Q[i7]==1 : basicColumns.append(i7)
    B = A[:,basicColumns]
    Xbfs = [i+theta*j for i,j in zip(Xbfs,d)]
print "Xbfs:",Xbfs
result = sum([i*j[0] for i,j in zip(Xbfs[:10],cList[:10])])
print result
