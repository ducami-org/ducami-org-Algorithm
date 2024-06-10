import math
def sum (a, b):
    return math.lcm(a, b)

a, b = map(int, input().split())
print(sum(a, b))