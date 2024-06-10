a,b,c,n=map(int,input().split())
if a==n:
    print(a)
else:
    for i in range(1,n):
        a=(a*b)+c
    print(a)