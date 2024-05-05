sum=0
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    sum+=a[i]
print(sum)