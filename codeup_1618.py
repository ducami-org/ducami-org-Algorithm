def sum(a):
    a = sorted(a)
    for i in range(len(a)):
        print(a[i], end=' ')
a = list(map(int, input().split()))
sum(a)