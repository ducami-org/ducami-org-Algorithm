a,b = map(int,input().split())
a = list(str(a))
b = list(str(b))
a_a = []
b_b = []
aa = 0
bb = 0
for i in range(2,-1,-1):
    a_a.append(a[i])
    b_b.append(b[i]) 
aa += int(a_a[0])*100 + int(a_a[1])*10 + int(a_a[2])
bb += int(b_b[0])*100 + int(b_b[1])*10 + int(b_b[2]) 
if aa > bb:
    print(aa)
else:
    print(bb)