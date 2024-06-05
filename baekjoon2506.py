n = int(input())
li = list(map(int,input().split()))
cnt = 0
sum = 0

for i in range(len(li)):
    if li[i] == 0:
        cnt = 0

    elif li[i] == 1:
        cnt = cnt + 1
        sum += cnt
print(sum)
