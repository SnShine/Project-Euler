import math, time

def Summationofprimes():
    a= 10
    for i in range(7, 2000000, 2):      #gives 109 seconds while (7, 2000000) gives 119 secs
        for j in range(2, int(math.sqrt(i))+1):
            if i%j== 0:
                break
        else:
            a+= i
        #print(a, i)
    print(a)
start= time.clock()
Summationofprimes()
end= time.clock()
print(end-start)