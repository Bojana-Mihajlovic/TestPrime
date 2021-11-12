from primenumber import is_prime 

def is_palindrome(x): 
    if is_prime(x)==True and len(str(x))==5 and str(x) == str(x) [::-1]:  
        output = []
        output.append(x)
        return  output
    else: 
        None 

