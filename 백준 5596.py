a = list(map(int, input().split()))
b = list(map(int, input().split()))
ar = 0
br = 0
for i in a:
    ar+=i
for i in b:
    br+=i
if ar>br:
    print(ar)
elif ar<br:
    print(br)
else:
    print(br)