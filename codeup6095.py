d = list()

for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)
        
a = int(input())
for i in range(a):
    c, e = map(int, input().split())
    d[c-1][e-1] = 1
    
for i in range(19):
    for k in range(19):
        print(d[i][k], end=' ')
    print()