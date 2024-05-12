n=int(input())
s=list(map(int,input().split()))
max=0
for i in s:
    if max<i:
        max=i

sum=0
for i in s:
    sum+=i/max*100
print(sum/n)

