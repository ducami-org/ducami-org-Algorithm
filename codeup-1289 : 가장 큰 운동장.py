l=[]
for _ in range(3):
    a,b=map(int,input().split())
    l.append(a*b)
print(max(l))