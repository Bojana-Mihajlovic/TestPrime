def deli(x): 
        delioci=[]
        m = list(range(1,100000)) 
        k=0
        while m[k]<=x:
                if x%m[k]==0:
                        delioci.append(m[k])
                else: 
                        None
                k+=1 
        return (delioci) 
 
