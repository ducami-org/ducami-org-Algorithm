li = []
sum = 0
cnt = 0
for i in range(7):
    a = int(input())
    if a % 2== 1:
        li.append(a)
        cnt += 1
        sum += a
if cnt > 0:
    print(sum)
    print(min(li))
else:
    print(-1)