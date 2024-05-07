sum = 0
for i in range(3):
    a,b = map(float,input().split())
    sum = sum + (a*b)
print(f"{sum:.1f}")