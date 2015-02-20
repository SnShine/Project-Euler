def ans():
    ans= []
    i= 1
    while True:
        p= int("".join(sorted(str(i**3)))[::-1])
        ans.append(p)
        print(i, p)
        if ans.count(p)== 5:
            print("answer: ", (ans.index(p)+1)**3)
            return
        
        i+= 1
        
ans()