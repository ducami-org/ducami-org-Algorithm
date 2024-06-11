def sum(q, a, b):
    sum = 0
    for i in range(0, q):
        if a[i] == b:
            sum = 1
            return i+1
    if sum == 0:
        return -1
q = int(input())
a = list(input().split())
b = input()
print(sum(q, a, b))