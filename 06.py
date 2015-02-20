def sumsquarediff():
    a, b= 0, 0
    for i in range(1,101):
        a+= i**2
        b+= i
    print(abs(a-(b**2)))

sumsquarediff()