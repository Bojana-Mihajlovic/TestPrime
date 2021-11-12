def deli(x): 
        delioci=[]
        m = list(range(1,x+1)) 
        k=0
        while k<=(x-1):
                if x%m[k]==0:
                        delioci.append(m[k])
                k+=1 
        return (delioci) 

print (deli(36643)) 