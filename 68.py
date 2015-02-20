import itertools

def magicring():
    arr= [1,2,3,4,5,6,7,8,9,10]
    ans= 1000000000000000
    for i in itertools.permutations(arr):
        i= list(i)
        i.append(i[5])
        p= i[0]+ i[0+ 5]+ i[0+ 6]
        for j in range(1, 5):
            if i[j]+ i[j+ 5]+ i[j+ 6]== p:
                continue
            else:
                break
        else:
            temp= []
            outi= sorted([i[k] for k in range(5)])
            kk= i.index(outi[0])
            pp= [0,1,2,3,4,0,1,2,3,4]
            for time in range(5):
                temp+= [i[pp[kk]], i[pp[kk]+ 5], i[pp[kk]+ 6]]
                kk+= 1
            
            temp= [str(p) for p in temp]
            if len("".join(temp))== 16:  
                ans= max((ans), int("".join(temp)))
                print(i, p, temp, ans)
            
    return

magicring()