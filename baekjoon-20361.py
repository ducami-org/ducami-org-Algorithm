a,b,c = map(int,input().split())
d=[i+1 for i in range(a)]
for i in range(c):
    x,y = map(int,input().split())
    temp = d[x-1]
    d[x-1] = d[y-1]
    d[y-1] = temp
print(d.index(b)+1)
# print(d)