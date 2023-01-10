{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a16be204",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/ns/5fsy_26d2ml4ys0kykxnrl000000gn/T/ipykernel_28405/2023693139.py:3: DeprecationWarning: Please use `pearsonr` from the `scipy.stats` namespace, the `scipy.stats.stats` namespace is deprecated.\n",
      "  from scipy.stats.stats import pearsonr\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "_vhstack_dispatcher() takes 1 positional argument but 2 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/ns/5fsy_26d2ml4ys0kykxnrl000000gn/T/ipykernel_28405/2023693139.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0mm\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmbill\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     35\u001b[0m \u001b[0mone\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mones\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mm\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 36\u001b[0;31m \u001b[0mx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhstack\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mone\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mmbill\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     37\u001b[0m \u001b[0mypred\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlocalWeightRegression\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mmtip\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0msortInd\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margsort\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<__array_function__ internals>\u001b[0m in \u001b[0;36mhstack\u001b[0;34m(*args, **kwargs)\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: _vhstack_dispatcher() takes 1 positional argument but 2 were given"
     ]
    }
   ],
   "source": [
    "from os import listdir\n",
    "from numpy import *\n",
    "from scipy.stats.stats import pearsonr\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "def kernel(pt,xmat,k):\n",
    "    m,n=np.shape(xmat)\n",
    "    wt=np.mat(np.eye(m))\n",
    "    for j in range(m):\n",
    "        diff=pt-x[j]\n",
    "        wt=np.exp(diff*diff.T/-2*k**2)\n",
    "        \n",
    "def localWeight(pt,xmat,ymat,k):\n",
    "    wei=kernel(pt,xmat,k)\n",
    "    wt=(x.T*(wei*x).I*(x.T*(wei*ymat.T)))\n",
    "    return wt\n",
    "\n",
    "def localWeightRegression(xmat,ymat,k):\n",
    "    m,n=np.shape(xmat)\n",
    "    ypred=np.zeros(m)\n",
    "    for i in range(m):\n",
    "        ypred[i]=xmat[i]*localWeight(xmat[i],xmat,ymat,k)\n",
    "    return ypred\n",
    "\n",
    "data=pd.read_csv('tips.csv')\n",
    "bill=np.array(data.total_bill)\n",
    "tip=np.array(data.tip)\n",
    "\n",
    "mbill=np.mat(bill)\n",
    "mtip=np.mat(tip)\n",
    "\n",
    "m=np.shape(mbill)[1]\n",
    "one=np.mat(np.ones(m))\n",
    "x=np.hstack(one.T,mbill.T)\n",
    "ypred=localWeightRegression(x,mtip,2)\n",
    "sortInd=x[:,1].argsort(0)\n",
    "xsort=x[sortInd][:,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "931f277d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np1\n",
    "\n",
    "def kernel(point,xmat, k):\n",
    "    m,n = np1.shape(xmat)\n",
    "    weights = np1.mat(np1.eye((m)))\n",
    "    for j in range(m):\n",
    "        diff = point - X[j]\n",
    "        weights[j,j] = np1.exp(diff*diff.T/(-2.0*k**2))\n",
    "    return weights\n",
    "def localWeight(point,xmat,ymat,k):\n",
    "    wei = kernel(point,xmat,k)\n",
    "    W=(X.T*(wei*X)).I*(X.T*(wei*ymat.T))\n",
    "    return W\n",
    "def localWeightRegression(xmat,ymat,k):\n",
    "    m,n = np1.shape(xmat)\n",
    "    ypred = np1.zeros(m)\n",
    "    for i in range(m):\n",
    "        ypred[i] = xmat[i]*localWeight(xmat[i],xmat,ymat,k)\n",
    "    return ypred\n",
    "# load data points\n",
    "data = pd.read_csv('tips1.csv')\n",
    "bill = np1.array(data.total_bill)\n",
    "tip = np1.array(data.tip)\n",
    "#preparing and add 1 in bill\n",
    "mbill = np1.mat(bill)\n",
    "mtip = np1.mat(tip)\n",
    "m= np1.shape(mbill)[1]\n",
    "one = np1.mat(np1.ones(m))\n",
    "X= np1.hstack((one.T,mbill.T))\n",
    "#set k here\n",
    "ypred = localWeightRegression(X,mtip,2)\n",
    "\n",
    "SortIndex = X[:,1].argsort(0)\n",
    "xsort = X[SortIndex][:,0]\n",
    "\n",
    "fig = plt.figure()\n",
    "ax = fig.add_subplot(1,1,1)\n",
    "ax.scatter(bill,tip, color='green')\n",
    "ax.plot(xsort[:,1],ypred[SortIndex], color = 'red', linewidth=5)\n",
    "plt.xlabel('Total bill')\n",
    "plt.ylabel('Tip')\n",
    "plt.show();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f452249e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}