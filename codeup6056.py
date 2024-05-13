a, b = map(int, input().split())
print(bool(a and (not b) or b and (not a)))