import numpy as np
with open('A_QP.txt','r') as f:
    AList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            AList.append(line)
with open('d_QP.txt','r') as f:
    dList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            dList.append(line)
with open('M_QP.txt','r') as f:
    MList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            MList.append(line)
with open('b_QP.txt','r') as f:
    bList = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            bList.append(line)

A = np.matrix(AList)
d = np.matrix(dList)
M = np.matrix(MList)
b = np.matrix(bList)
m,n = M.shape
temp1 = np.concatenate((A,-M.T),axis=1)
temp2 = np.concatenate((M,np.zeros((m,m))),axis=1)
K = np.concatenate((temp1,temp2),axis=0)
temp3 = np.concatenate((-d,b),axis=0)

result = K.getI()*temp3
X = result[:n]
print X
np.savetxt('xkkt.txt',X,fmt='%2.2f')
