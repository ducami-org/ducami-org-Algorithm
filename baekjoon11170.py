n = int(input())
cnt = 0
for i in range(n):
    cnt = 0
    a,b = map(int,input().split())
    for j in range(a,b+1):
        j = list(str(j))
        cnt += j.count('0')
    print(cnt)

