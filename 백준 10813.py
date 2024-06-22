li = []
num, sum = map(int, input().split())
for i in range(num):
    li.append(i+1)
temp = 0
for i in range(sum):
    a, b = map(int, input().split())
    temp = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = temp
for i in li:
    print(i, end=' ')