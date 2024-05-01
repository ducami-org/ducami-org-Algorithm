a,b = map(int,input().split())
d=list()
total =0
for i in range(a):
    d.append([])
    for j in range(b):
        d[i].append(0)
        
for i in range(a):
    d[i] = input()
    
for i in range(a):
    O =0
    for j in range(b):
        if(d[i][j]=='O'):
            O +=1
        
    if(O>=b//2+1):
        total +=1
        
        
print(total)