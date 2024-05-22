a=set()
b=set()
def num(n,m):
    for i in range(1,n+1):
        if n%i==0:
            a.add(i)
    for i in range(1,m+1):
        if m%i==0:
            b.add(i)
    return max(a&b)
n,m=map(int,input().split())
print(num(n,m))
            
        
