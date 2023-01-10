class G:
    def __init__(self,al):
        self.al=al
        
    def gn(self,v):
        return al[v]
    
    def heu(self,n):
        h={'A':1,
           'B':1,
           'C':1,
           'D':1,
          }
        return h[n]
    
    def astar(self,start,stop):
        ol=set([start])
        cl=set([])
        
        poo={}
        poo[start]=0
        
        par={}
        par[start]=start
        while len(ol)>0:
            n=None
            for v in ol:
                if n==None or poo[v]+self.heu(v)<poo[n]+self.heu(n):
                    n=v

            if n==None:
                print("Path does not exist")
                return None

            if n==stop:
                rp=[]
                while par[n]!=n:
                    rp.append(n)
                    n=par[n]
                rp.append(start)
                rp.reverse()
                print("Path exists",rp)
                return rp
            
            for (m,wt) in self.gn(n):
                if m not in ol and m not in cl:
                    ol.add(m)
                    par[m]=n
                    poo[m]=poo[n]+wt
                    
                else:
                    if poo[m]>poo[n]+wt:
                        poo[m]=poo[n]+wt
                        par[m]=n
                        
                        if m in cl:
                            cl.remove(m)
                            ol.add(m)
                            
            ol.remove(n)
            cl.add(n)
            
        
al={'A':[('B',10),('C',5),('D',7)],
    'B':[('D',2)],
    'C':[('D',1)]
   }

g1=G(al)
g1.astar('A','D')
