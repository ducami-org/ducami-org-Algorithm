def f(n):
    if n<=1:
        return 1
    else:
        result=n*f(n-1)
        return result
    
print(f(int(input())))