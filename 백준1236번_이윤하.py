n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(input().strip()))

sum=0
cnt=0
for i in range(n):
    if 'X' not in arr[i]:
        sum+=1
cnt2=0
for j in range(m):
    cnt=True
    for i in range(n):
        if arr[i][j]=='X':
            cnt=False
            break

    if cnt:
        cnt2+=1
print(max(sum,cnt2))