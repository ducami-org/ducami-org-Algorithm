a = int(input())
f=0
m=0
for i in range(a):
    b = list(input().split(','))
    for i in b:
        if(i=='F'):
            f+=1
            break
        if(i=='M'):
            m+=1
            break
print(m)
print(f)