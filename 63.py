ans= 0

for power in range(1, 100):
    for number in range(1, 10):
        if len(str(number**power))== power:
            #print(number, power)
            ans+= 1
            
print(ans)