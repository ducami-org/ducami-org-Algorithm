def f(n):
    if n<=0:
        return
    else:
        print(n)
        f(n-1)
n=int(input())
f(n)