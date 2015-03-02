import time
triangle= [int(i*(i+1)/2) for i in range(30)]

def value(s):
    ans= 0
    for i in s:
        ans+= ord(i)-64
        
    return ans

def coded():
    file= open('p042_words.txt', 'r')
    a= file.read().split(",")
    print(a)
    ans= 0
    
    for i in range(len(a)):
        p= value(a[i][1:-1])
        if p in triangle:
            ans+= 1
    
    print(ans)
    return
st= time.clock()
coded()
print(time.clock()-st)