hap = 0
b=[]
for i in range(7):
    a = int(input())
    if a % 2 !=0:
        b.append(a)
        hap += a
if len(b) == 0:
    print(-1)
else:
    print(hap)
    print(min(b))
