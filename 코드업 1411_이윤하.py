n=int(input())
l=list(range(1,n+1))

for i in range(n-1):
    m=int(input())
    if m in l:
        l.remove(m)
for i in l:
    print(i)
    
        