from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris=datasets.load_iris()
x=pd.DataFrame(iris.data)
x.columns=['Sepakl_Length','Sepal_Width','Petal_Length','Petal_Width']
print(x)
y=pd.DataFrame(iris.target)
y.columns=['Target']
print(y)

model=KMeans(n_clusters=3)
model.fit(x)

plt.figure(figsize=(14,14))
colormap=np.array(['red','lime','blue'])

plt.subplot(2,2,1)
plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[y.Target],s=40)
plt.title('Real Cluster')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.subplot(2,2,2)
plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[model.labels_],s=40)
plt.title('KMeans Cluster')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

from sklearn import preprocessing as p
scaler=p.StandardScaler()
scaler.fit(x)
xst=scaler.transform(x)
xs=pd.DataFrame(xst,columns=x.columns)

from sklearn.mixture import GaussianMixture
gmm=GaussianMixture(n_components=3)
gmm.fit(xs)
gmm_y=gmm.predict(xs)
plt.subplot(2,2,3)
plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[gmm_y],s=40)
plt.title('KMeans Cluster')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
