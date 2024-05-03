a,b = map(int,input().split())
max = a+b
if(a-b>max):
    max=a-b
if(b-a>max):
    max=b-a
if(a*b>max):
    max=a*b
if(a/b>max):
    max=a/b
if(b/a>max):
    max=b/a
if(a**b>max):
    max = a**b
if(b**a>max):
    max = b**a 
print(f"{max:.6f}")   