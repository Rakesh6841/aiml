import numpy as np1
import pandas as pd
import matplotlib.pyplot as plt

def kernel(p,xm,k):
    (m,n)=np1.shape(xm)
    w=np1.mat(np1.eye(m))
    for j in range(m):
        d=p-X[j]
        w[j,j]=np1.exp(d*d.T/(-2*k**2))
    return w

def lw(p,xm,ym,k):
    wei=kernel(p,xm,k)
    w=(X.T*(wei*X)).I*(X.T*(wei*ym.T))
    return w

def lwr(xm,ym,k):
    (m,n)=np1.shape(xm)
    ypred=np1.zeros(m)
    for i in range(m):
        ypred[i]=xm[i]*lw(xm[i],xm,ym,k)
    return ypred

data=pd.read_csv('tips1.csv')
b=data['total_bill']
t=data['tip']

mb=np1.mat(b)
mt=np1.mat(t)

m=np1.shape(mb)[1]
one=np1.mat(np1.ones(m))
X=np1.hstack((one.T,mb.T))
si=X[:,1].argsort(0)
xs=X[si][:,0]

ypred=lwr(X,mt,2)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(b,t,color='green')
ax.plot(xs[:,1],ypred[si],c='red',lw=5)
