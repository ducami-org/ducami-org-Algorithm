def sum(a):
    a.sort()
    return a[1]
a= list(map(int, input().split()))
print(sum(a))