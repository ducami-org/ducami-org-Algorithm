def sum(b, c):
    sum = b[c[0]-1]
    sumindex = c[0]
    for i in range(c[0]-1, c[1]):
        if sum < b[i]:
            sumindex = i+1
            sum = b[i]
    return sumindex
a = int(input())
b = list(map(int, input().split()))
c = list(map(int,input().split()))
print(sum(b, c))