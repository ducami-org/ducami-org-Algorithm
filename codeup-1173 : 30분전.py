a,b=map(int,input().split())
if a==0 and b<30:
    print(f"{23} {60-30+b}")
elif b<30:
    print(f"{a-1} {b+60-30}")
else:
    print(f"{a} {b-30}")