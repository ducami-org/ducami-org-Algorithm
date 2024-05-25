n=int(input())
tot=0
arr=list(map(int,input().split()))
for i in range(n):
    tot+=arr[i]

print(tot)
