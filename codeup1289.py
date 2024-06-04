max_n = 0
for i in range(3):
    a,b = map(int,input().split())
    if a*b > max_n:
        max_n = a*b
print(max_n)