a = int(input())
total=a
b= int(input())
c = list(map(int,input().split()))
for i in range(b):
    a = a*(100+c[i])/100
if(a-total>0):
    print(f"{a-total:.0f}")
    print('good')
elif(a-total==0):
    print(f"{a-total:.0f}")
    print('same')
else:
    print(f"{a-total:.0f}")
    print('bad')
    