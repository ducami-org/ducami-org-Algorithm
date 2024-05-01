a =int(input())
d= list(0 for i in range(10000))
for i in range(a):
    b= int(input())
    d[b-1]+=1
    
for i in range(a):
    for j in range(d[i]):
        print(i+1)