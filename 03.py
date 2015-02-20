import math

def largeprimefactor():
    num= 600851475143
    a= []
    for i in range(6, int(600851475143/2)):
        for j in range(2, int(math.sqrt(i)+1)):
            if i%j == 0:
                break
        else:
            if i> num:
                break
            if num%i== 0:
                num/= i
                a.append(i)
                #print(a)
    
    print(max(a))
    
largeprimefactor()      