a, b = map(int,input().split())
d=[0 for i in range(0,b-a+1)]
total =[1 for i in range(0, b-a+1)]
num=0

for i in range(0,b-a+1):
    d[i] = a+i

for i in range(0, b-a+1):
    c = a+i
    while(c!=1):
        total[i]+=1
        if(c%2==0):
            c = c/2
        else:
            c = (c*3)+1

for i in range(0, len(total)):
    if(total[i] == max(total)):
        num = i
        break
        
print(d[num], max(total))
