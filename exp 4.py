import math
import numpy as np
import pandas as pd

data=pd.read_csv('exp4.csv')
feature=[feat for feat in data]
feature.remove("classification")

class Node:
    def __init__(self):
        self.child=[]
        self.value=""
        self.leaf=False
        self.pred=""
        
def e(exam):
    pos=0.0
    neg=0.0
    for _,row in exam.iterrows():
        if row["classification"]=="Yes":
            pos+=1
        else:
            neg+=1
    if pos==0.0 or neg==0.0:
        return 0
    p=pos/(pos+neg)
    n=neg/(pos+neg)
    return -(p*math.log(p,2)+n*math.log(n,2))

def ig(exam,attr):
    g=e(exam)
    uniq=np.unique(exam[attr])
    for u in uniq:
        sd=exam[exam[attr]==u]
        se=e(sd)
        g-=(float(len(sd))/float(len(exam)))*se
    return g

def id3(exam,attr):
    root=Node()
    mf=""
    mg=0
    
    for f in attr:
        g=ig(exam,f)
        if g>mg:
            mg=g
            mf=f
            
    root.value=mf
    
    uniq=np.unique(exam[mf])
    for u in uniq:
        sd=exam[exam[mf]==u]
        if e(sd)==0:
            n=Node()
            n.leaf=True
            n.value=u
            n.pred=np.unique(sd["classification"])
            root.child.append(n)
            
        else:
            d=Node()
            d.value=u
            na=attr.copy()
            na.remove(mf)
            c=id3(sd,na)
            d.child.append(c)
            root.child.append(d)
            
    return root

def pt(root:Node(),d=0):
    for i in range(d):
        print("\t",end="")
    print(root.value,end="")
    if root.leaf:
        print("->",root.pred)
    print()
    for c in root.child:
        pt(c,d+1)
        
root=id3(data,feature)
pt(root)
