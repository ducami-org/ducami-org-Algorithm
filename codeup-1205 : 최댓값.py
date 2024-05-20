a,b=map(int,input().split())
c=a+b
if b+a>c:
    c=b+a

if a-b>c:
    c=a-b
if b-a>c:
    c=b-a

if a*b>c:
    c=a*b
    
if a/b>c:
    c=a/b
if b/a>c:
    c=b/a
if a**b>c:
    c=a**b
    
if b**a>c:
    c=b**a
    
print(f"{c:.6f}")