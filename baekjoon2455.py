sum = 0
max_sum = 0
for i in range(4):
    a,b = map(int,input().split())
    sum -= a
    sum+= b
    if i == 3:
        break
    if sum > max_sum:
        max_sum = sum

print(max_sum)