result = 0
a = int(input())
b = list(map(int, input().split()))
b.sort()
for i in range(a):
    result += b[i]/b[-1]*100
print(result/a)