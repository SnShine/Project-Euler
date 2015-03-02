import math

def trianglenumber(n):      #sigma function
    return (n*(n+1))/2

def divisors(n):
    ans= 0
    i= 1
    while i<= math.sqrt(n):
        if n%i== 0:
            if i!= int(n/i):
                ans+= 2
            if i== int(n/i):
                ans+= 1
        i+= 1
    return ans


for k in range(12000, 20000):
    #print(k, trianglenumber(k), divisors(trianglenumber(k)))
    if divisors(trianglenumber(k))> 500:
        print(k, trianglenumber(k), divisors(trianglenumber(k)), "Completed!")
        break