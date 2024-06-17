a = int(input())
b = list(map(int, input().split()))
M = max(b)
for i in range(a):
    b[i] = b[i]/M*100

print(sum(b)/a)