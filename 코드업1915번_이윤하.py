
def f(s,n):
   
    if s==0:
        return 0
    elif s==1:
        return 1
    
    else:
        result=f(s-1,n)+f(s-2,n)
        return result
    
n=int(input())
print(f(n,n))