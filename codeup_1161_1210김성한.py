a, b = map(int, input().split())
c = int(a+b)
if a % 2 == 0:
    a = "짝수"
else:
    a = "홀수"
if b % 2 == 0:
    b = "짝수"
else:
    b = "홀수"
if c % 2 == 0:
    c = "짝수"
else:
    c = "홀수"
print(f"{a}+{b}={c}")
