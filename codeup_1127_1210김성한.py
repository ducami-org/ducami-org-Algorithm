sum = 0
for i in range(3):
    a,b =input().split()
    sum = sum+float(a)*int(b)
print(f"{sum:.1f}")