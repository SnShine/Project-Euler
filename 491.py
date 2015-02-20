import itertools, time, math        #correct answer

def ans():
    ans= 0
    for i in set((itertools.combinations("99887766554433221100", 10))):
        if abs(90-(2*sum([int(j) for j in i])))%11== 0:    
            pairs= 10- len(set([k for k in i]))
            zeros= i.count("0")
            
            allways= math.factorial(10)/(2**pairs)
            onezeroway= (allways)- (math.factorial(9)/(2**pairs))
            twozeroway= (allways)- (math.factorial(9)/(2**(pairs-1)))
            
            if zeros== 0:
                ans+= allways*(allways)
            elif zeros== 1:
                ans+= allways*(onezeroway)
            elif zeros== 2:
                ans+= allways*(twozeroway)
                
    print(int(ans))
    return

st= time.clock()
ans()
print(time.clock()-st)
