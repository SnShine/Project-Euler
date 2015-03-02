import math

def stprime():
    a= True
    num= 5
    ans= 3
    while(a):
        num+= 2
        for j in range(2, int(math.sqrt(num)+1)):
            if num%j== 0:
                break
        else:
            ans+= 1
        #print(ans)
        if ans== 10001:
            print(num)
            a= False

stprime()