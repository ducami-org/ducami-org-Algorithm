def f(n):
    if n==1:
        return 1
    return f(n-1)+n
while True:
    n=int(input())
    if n==0:
        break
    else:
        print(f(n))
