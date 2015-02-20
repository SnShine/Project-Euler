def fibonacci():
    a, b= 0, 1
    ans= []
    while a< 4000000:
        if a%2== 0:
            ans.append(a)
        a, b= b, a+b
    
    print(sum(ans))
fibonacci()