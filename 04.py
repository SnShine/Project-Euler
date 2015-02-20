def palindrome():
    #999*999
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            a= i*j
            #print(a)
            st= str(a)
            #print(st)
            #print(st[:], st[::-1])
            if st[:]== st[::-1]:
                print(st)
                return

palindrome()