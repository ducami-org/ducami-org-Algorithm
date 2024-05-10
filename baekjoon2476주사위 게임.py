t = int(input())
cnt_sum = [0]*t
cnt = 0
for i in range(t):
    cnt = 0
    a,b,c = map(int,input().split())
    if a == b == c:
        cnt += 10000+(a*1000)
    elif a==b:
        cnt += 1000+(a*100)
    elif b == c:
        cnt += 1000+(b*100)
    elif a==c:
        cnt += 1000+(c*100)
    else:
        cnt += max(a,b,c)*100
    cnt_sum[i] = cnt
print(max(cnt_sum))
