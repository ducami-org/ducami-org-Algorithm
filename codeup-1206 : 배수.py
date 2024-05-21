a,b=map(int,input().split())
if a%b==0:
    print(f"{a}*{(int(a/b))}={b}")
elif b%a==0:
    print(f"{a}*{int(b/a)}={b}")
else:
    print("none")
