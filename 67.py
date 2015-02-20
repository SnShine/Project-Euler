import time
def path():                         #same as problem 18
    a= []                           #same as assembly line scheduling, CLRS first model of DP
    n= 100                          #number of rows in pyramid
    for i in range(n):
        a.append([int(k) for k in input().split()])
    st= time.clock()
    a[1][0], a[1][-1]= a[1][0]+ a[0][0], a[1][-1]+ a[0][0]
    
    for i in range(2, n):
        a[i][0], a[i][-1]= a[i-1][0]+ a[i][0], a[i-1][-1]+ a[i][-1]
        for j in range(1, i):
            a[i][j]= max(a[i-1][j-1], a[i-1][j])+ a[i][j]
    #print(a)
    print(max(a[-1]))
    print(time.clock()- st)
    return

path()