n=int(input())
l=list(map(int,input().split()))
max=0
min=101
for i in range(n):
    if max<l[i]:
        max=l[i]
    if min>l[i]:
        min=l[i]
print(max,min)