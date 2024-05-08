a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
be = 0
for i in range(0, 6):
    for j in range(0,6):
        if a[i] == b[j]:
            sum+=1
for i in range(0, 6):
    if a[6] == b[i]:
        be+=1
if sum >= 6: 
    print(1)
elif sum==5 and be>=1:
    print(2)
elif sum==5:
    print(3)
elif sum ==4:
    print(4)
elif sum ==3:
    print(5)
else:
    print(0)