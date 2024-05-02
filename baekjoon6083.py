#내 답안
r,g,b, = map(int,input().split())
for i in range(r):
    for j in range(g):
        for f in range(b):
            print(i,j,f)
print(r*g*b)
#다른 답안
r, g, b = map(int,input().split())

count=0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print('%d %d %d' %(i,j,k))
            
            count = count + 1
            
print(count)