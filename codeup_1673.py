import math
a = list(map(int, input().split()))
sorted(a)
print(math.gcd(a[0], a[1], a[2]))