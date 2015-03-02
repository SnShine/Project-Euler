def Pythagoreantriplet():
    for c in range(1000, 333, -1):
        for a in range(1, int((1000-c)/2 + 1)):
            if c**2== (a**2)+(1000-c-a)**2:
                print(a*(1000-c-a)*c)
                print(a, 1000-c-a, c)

Pythagoreantriplet()