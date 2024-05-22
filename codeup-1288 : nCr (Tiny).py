def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return n*f(n-1)

n,m=map(int,input().split())
a,b,c=f(n),f(n-m),f(m)

if b==0:
    print(int(a/c))
else:
    print(int(a/(b*c)))