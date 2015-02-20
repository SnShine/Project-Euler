def multiples35():
    mul3= [3*i for i in range(int(1000/3) + 1)]
    mul5= [5*i for i in range(int(1000/5) + 1)]
    if 1000 in mul5:
        mul5.remove(1000)
        
    ans= sum(set(mul3+mul5))
    print(ans)

multiples35()