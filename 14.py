maxans= 0
mine = 0
for i in range(10, 1000000):
    ans= 0
    p= i
    while i>2:
        if i%2== 0:
            i=i/2
        else:
            i= 3*i + 1
        ans+= 1
    if ans> maxans:
        maxans= ans
        mine= p
    
    print(p)

print(mine, maxans)
        