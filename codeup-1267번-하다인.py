a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    if i%5==0:
        s+=i
print(s)