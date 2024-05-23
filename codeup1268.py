n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(len(a)):
    if a[i]%2==1:
        cnt += 1
print(cnt)