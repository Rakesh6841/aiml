{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "18a97640",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'A'}\n",
      "v A  n None\n",
      "{'D', 'B', 'C'}\n",
      "v D  n None\n",
      "v B  n D\n",
      "v C  n B\n",
      "{'D', 'C'}\n",
      "v D  n None\n",
      "v C  n D\n",
      "{'D'}\n",
      "v D  n None\n",
      "Path found ['A', 'B', 'D']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['A', 'B', 'D']"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from collections import deque\n",
    "\n",
    "class Graph:\n",
    "\n",
    "    def __init__(self,al):\n",
    "        self.al=al\n",
    "\n",
    "    def gn(self,v):\n",
    "        return self.al[v]\n",
    "    \n",
    "    def h(self,n):\n",
    "        heu={\n",
    "            'A':1,\n",
    "            'B':1,\n",
    "            'C':1,\n",
    "            'D':1\n",
    "        }\n",
    "        return heu[n]\n",
    "    \n",
    "    def astar(self,start,stop):\n",
    "        ol=set([start])\n",
    "        cl=set([])\n",
    "        \n",
    "        poo={}\n",
    "        poo[start]=0\n",
    "        \n",
    "        par={}\n",
    "        par[start]=start\n",
    "        \n",
    "        while len(ol)>0:\n",
    "            n=None\n",
    "            print(ol)\n",
    "            for v in ol:\n",
    "                print('v',v,' n',n)\n",
    "                if n==None or poo[v]+self.h(v)<poo[n]+self.h(n):\n",
    "#                     print('poo v')\n",
    "                    n=v\n",
    "\n",
    "#             print(n)\n",
    "            if n==None:\n",
    "                print(\"Path does not exist\")\n",
    "                return None\n",
    "            \n",
    "            if n==stop:\n",
    "                rp=[]\n",
    "                while par[n]!=n:\n",
    "                    rp.append(n)\n",
    "                    n=par[n]\n",
    "                    \n",
    "                rp.append(start)\n",
    "                rp.reverse()\n",
    "                \n",
    "                print(\"Path found\",rp)\n",
    "                return rp\n",
    "            \n",
    "            for (m,wt) in self.gn(n):\n",
    "#                 print(m)\n",
    "                if m not in ol and m not in cl:\n",
    "                    ol.add(m)\n",
    "                    par[m]=n\n",
    "                    poo[m]=poo[n]+wt\n",
    "                    \n",
    "                else:\n",
    "                    if poo[m]>poo[n]+wt:\n",
    "                        poo[m]=poo[n]+wt\n",
    "                        par[m]=n\n",
    "                        \n",
    "                        if m in cl:\n",
    "                            cl.remove(m)\n",
    "                            ol.add(m)\n",
    "                            \n",
    "            ol.remove(n)\n",
    "            cl.add(n)\n",
    "#             print(ol)\n",
    "#             print(cl)\n",
    "            \n",
    "        print(\"Path does not exist hello\")\n",
    "        return None\n",
    "    \n",
    "    \n",
    "al={'A':[('B',1),('C',3),('D',7)],\n",
    "    'B':[('D',5)],\n",
    "    'C':[('D',12)]\n",
    "   }\n",
    "\n",
    "g1=Graph(al)\n",
    "g1.astar('A','D')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ab290be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5d7d559",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31f8286b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ac05e4e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cdae52c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "116ef107",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85b8bb0d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6f7b12a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e76607b8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96e6b535",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "072746c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e391666",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c86ac67",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89f7656a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "1da24356",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Path exists:  ['A', 'B', 'D']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['A', 'B', 'D']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "class Graph:\n",
    "    \n",
    "    def __init__(self,al):\n",
    "        self.al=al\n",
    "        \n",
    "    def gn(self,v):\n",
    "        return self.al[v]\n",
    "    \n",
    "    def h(self,n):\n",
    "        H={'A':1,\n",
    "           'B':1,\n",
    "           'C':1,\n",
    "           'D':1\n",
    "          }\n",
    "        return H[n]\n",
    "    \n",
    "    def astar(self,start,stop):\n",
    "        ol=set([start])\n",
    "        cl=set([])\n",
    "        \n",
    "        poo={}\n",
    "        poo[start]=0\n",
    "        \n",
    "        par={}\n",
    "        par[start]=start\n",
    "        \n",
    "        while len(ol)>0:\n",
    "            n=None\n",
    "            \n",
    "            for v in ol:\n",
    "                if n==None or poo[v]+self.h(v)<poo[n]+self.h(v):\n",
    "                    n=v\n",
    "            \n",
    "            if n==None:\n",
    "                print(\"Path does not exist\")\n",
    "                return None\n",
    "            \n",
    "            if n==stop:\n",
    "                rp=[]\n",
    "                while par[n]!=n:\n",
    "                    rp.append(n)\n",
    "                    n=par[n]\n",
    "                    \n",
    "                rp.append(start)\n",
    "                rp.reverse()\n",
    "                \n",
    "                print(\"Path exists: \",rp)\n",
    "                return rp\n",
    "            \n",
    "        \n",
    "            for (m,wt) in self.gn(n):\n",
    "                if m not in ol and m not in cl:\n",
    "                    ol.add(m)\n",
    "                    par[m]=n\n",
    "                    poo[m]=poo[n]+wt\n",
    "\n",
    "                else:\n",
    "                    if poo[m]>poo[n]+wt:\n",
    "                        poo[m]=poo[n]+wt\n",
    "                        par[m]=n\n",
    "\n",
    "                        if m in cl:\n",
    "                            cl.remove(m)\n",
    "                            ol.add(m)\n",
    "\n",
    "            ol.remove(n)\n",
    "            cl.add(n)\n",
    "        \n",
    "\n",
    "al={'A':[('B',2),('C',8),('D',10)],\n",
    "    'B':[('D',5)],\n",
    "    'C':[('D',1)]\n",
    "   }\n",
    "        \n",
    "graph1=Graph(al)\n",
    "graph1.astar('A','D')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7144c35",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dbdf2d8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6989c146",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c2665ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "017f8c7b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7708850c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c3f7790",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "caf6000f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee9df00b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d289c03d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcd81757",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "2ec37242",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Path exists ['A', 'C', 'D']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['A', 'C', 'D']"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class G:\n",
    "    def __init__(self,al):\n",
    "        self.al=al\n",
    "        \n",
    "    def gn(self,v):\n",
    "        return al[v]\n",
    "    \n",
    "    def heu(self,n):\n",
    "        h={'A':1,\n",
    "           'B':1,\n",
    "           'C':1,\n",
    "           'D':1,\n",
    "          }\n",
    "        return h[n]\n",
    "    \n",
    "    def astar(self,start,stop):\n",
    "        ol=set([start])\n",
    "        cl=set([])\n",
    "        \n",
    "        poo={}\n",
    "        poo[start]=0\n",
    "        \n",
    "        par={}\n",
    "        par[start]=start\n",
    "        while len(ol)>0:\n",
    "            n=None\n",
    "            for v in ol:\n",
    "                if n==None or poo[v]+self.heu(v)<poo[n]+self.heu(n):\n",
    "                    n=v\n",
    "\n",
    "            if n==None:\n",
    "                print(\"Path does not exist\")\n",
    "                return None\n",
    "\n",
    "            if n==stop:\n",
    "                rp=[]\n",
    "                while par[n]!=n:\n",
    "                    rp.append(n)\n",
    "                    n=par[n]\n",
    "                rp.append(start)\n",
    "                rp.reverse()\n",
    "                print(\"Path exists\",rp)\n",
    "                return rp\n",
    "            \n",
    "            for (m,wt) in self.gn(n):\n",
    "                if m not in ol and m not in cl:\n",
    "                    ol.add(m)\n",
    "                    par[m]=n\n",
    "                    poo[m]=poo[n]+wt\n",
    "                    \n",
    "                else:\n",
    "                    if poo[m]>poo[n]+wt:\n",
    "                        poo[m]=poo[n]+wt\n",
    "                        par[m]=n\n",
    "                        \n",
    "                        if m in cl:\n",
    "                            cl.remove(m)\n",
    "                            ol.add(m)\n",
    "                            \n",
    "            ol.remove(n)\n",
    "            cl.add(n)\n",
    "            \n",
    "        \n",
    "al={'A':[('B',10),('C',5),('D',7)],\n",
    "    'B':[('D',2)],\n",
    "    'C':[('D',1)]\n",
    "   }\n",
    "\n",
    "g1=G(al)\n",
    "g1.astar('A','D')\n",
    "    \n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0945d99",
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
