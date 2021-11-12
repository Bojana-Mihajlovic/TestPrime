from primenumber import is_prime 


def primes_below(n): 
    output=[]
    x=1
    while x<n: 
        if is_prime(x)==True: 
            output.append(x)
        x +=1 
    return output 



