def f(a,b):
    if(b==1):
        return 1    
    if(a==b):
        return 1
    return f(a-1,b-1)+f(a-1,b)
    
a,b = map(int,input().split())
print(f(a,b))