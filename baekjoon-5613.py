d=[]
while True:
    a = input()
    d.append(a)
    if(a=='='):
        break
    
total =0; d[0] = int(d[0])
for i in range(len(d)):
    if(d[i]=='='):
        break
    if(d[i]=='+'):
        d[0] += int(d[i+1])
    elif(d[i]=='-'):
        d[0] -= int(d[i+1])
    elif(d[i]=='*'):
        d[0] *= int(d[i+1])
    elif(d[i]=='/'):
        d[0] //= int(d[i+1])
print(d[0])