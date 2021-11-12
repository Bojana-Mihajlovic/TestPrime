
from is_palindrome import is_palindrome

result=[]
x= 10000
while x<100000: 
    if is_palindrome(x)!=None: 
        result.append(x)
    x+=1 
    print (result) 


    
