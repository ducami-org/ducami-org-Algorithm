a, b = map(int, input().split())
count = 0
for ii in range(a, b+1):
    if ii % 3 == 0:
        count += ii
print(count)
