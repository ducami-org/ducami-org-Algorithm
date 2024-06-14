def f(n,m):
    if m>n:
        return m-n
    
    else:
        return n-m
n,m=map(int,input().split())
print(f(n,m))