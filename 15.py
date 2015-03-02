a= [i for i in range(1, 22)]
#print(a)
b= [1]

for j in range(19):
    for i in range(1, 21):
        #print(i, b)
        b.append(a[i]+b[i-1])
        #print(b)
    a= b
    b= [1]
    #print(a)

print(a[-1])
    