from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as tts
import numpy as np

iris=load_iris()
t=iris.target_names
for i in range(len(target)):
    print(target[i],i)
    
xtr,xte,ytr,yte=tts(iris['data'],iris['target'])
kn=knn(1)
kn.fit(xtr,ytr)

for i in range(len(xte)):
    xn=np.array([xte[i]])
    p=kn.predict(xn)
    print('actual {0}{1} , predicted {2}{3}'.format(yte[i],t[yte[i]],p,t[p]))
