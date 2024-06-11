def sum(q, a, b):
    temp = 0
    sum = 0
    for i in range(0, q):
        if a[i] >= b:
            if temp == 0:
                temp = i+1
        else:
            sum+=1
    if sum == q:
        return q+1
    else:
        return temp
q = int(input())
a = list(map(int, input().split()))
b = int(input())
print(sum(q, a, b))