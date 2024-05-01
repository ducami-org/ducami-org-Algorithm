d=['N','E','S','W']
e=[0 for i in range(3)]
for _ in range(10):
    b =int(input())
    e[b-1]+=1
    
e[1] %= 2
i = e[1]*2

i+= (e[0]-e[2])

if(i<0):
    
if(i>=4):
    i %=4
    
print(d[i])