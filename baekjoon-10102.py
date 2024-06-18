a = int(input())
b = input()
d=[0,0]
for i in b:
    if(i=='A'):
        d[0]+=1
    else:
        d[1]+=1
        
if(d[0]>d[1]):
    print('A')
elif(d[1]>d[0]):
    print('B')
else:
    print('Tie')