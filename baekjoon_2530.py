a = list(map(int, input().split()))
b = int(input())
for i in range(1, b+1):
    a[2] += 1
    if a[2] == 60:
        a[1] += 1
        a[2] = 0
        if a[1] == 60:
            a[0] += 1
            a[1] = 0
            if a[0] == 24:
                a[0] = 0
print(a[0], a[1], a[2])