a, b, c, d = map(int, input().split())
aa = a*b*c*d/8/1024/1024
print(f"{aa:.1f} MB")