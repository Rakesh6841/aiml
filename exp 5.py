import numpy as np

inpn=2
hidln=4
outn=2
itr=6000

inp=np.random.randint(1,5,inpn)
out=[1.0,0.0]
hidl=np.random.randint(1,hidln)

hidb=np.random.rand(1,hidln)
outb=np.random.rand(1,outn)
hidw=np.random.rand(inpn,hidln)
outw=np.random.rand(hidln,outn)

def sig(x):
    return 1/(1+np.exp(-x))

def grad(x):
    return x*(1-x)

for i in range(itr):
    
    hidl=np.dot(inp,hidw)
    hidl=sig(hidl)
    outl=np.dot(hidl,outw)
    outl=sig(outl)
    
    e=out-outl
    gout=grad(outl)
    eto=gout*e
    eth=grad(hidl)*np.dot(eto,outw.T)
    
    ghidw=np.dot(inp.reshape(inpn,1),eth.reshape(1,hidln))
    goutw=np.dot(hidl.reshape(hidln,1),eto.reshape(1,outn))
    
    hidw+=0.5*ghidw
    outw+=0.5*goutw
    
    if i<50 or i>itr-50:
        print('error: ',e)
        print('output: ',outl)
