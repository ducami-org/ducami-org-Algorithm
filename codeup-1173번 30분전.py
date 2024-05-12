a,b = map(int, input().split())
if b - 30 < 0:
    b = 60 + (b - 30)
    
    if a - 1 < 0:
        a = 23
    else:
        a -= 1
else:
    b -= 30

print(a, b)