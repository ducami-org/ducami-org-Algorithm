n,m = map(int,input().split())
baguni = [0 for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    for j in range(a-1,b):
        baguni[j] = c

for i in baguni:
    print(i,end=' ')