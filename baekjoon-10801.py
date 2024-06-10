a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1=0
b1=0
tie=0
for i in range(len(a)):
    if(a[i]>b[i]):
        a1+=1
    elif(a[i]<b[i]):
        b1+=1
    else:
        tie+=1
        
if(a1>b1):
    print('A')
elif(a1<b1):
    print('B')
else:
    print('D')