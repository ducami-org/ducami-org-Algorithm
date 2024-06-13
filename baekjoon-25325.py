a = int(input())
name = list(input().split())
d=[0 for _ in range(a)]
for i in range(a):
    b = list(input().split())
    for j in b:
        d[name.index(j)]+=1
        
for i in range(a):
    print(name[d.index(max(d))],max(d))
    d[d.index(max(d))]= -1
    