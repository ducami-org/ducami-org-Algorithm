a, b = map(int, input().split())
c = list(range(1, a+1))
temp = []
for i in range(b):
    n, m =  map(int, input().split())
    temp=[]
    for j in range(n-1, m):
        temp.append(c[j])
    temp.reverse()
    for z in range(n-1, m):
        c[z] = temp[z-n+1]
for i in c:
    print(i, end=' ')