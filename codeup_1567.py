def sum(a, b, c):
    sum = 0
    for i in range(c[0]-1, c[1]):
        sum+=b[i]
    return sum
a = int(input())
b = list(map(int, input().split()))
c = list(map(int,input().split()))
print(sum(a, b, c))