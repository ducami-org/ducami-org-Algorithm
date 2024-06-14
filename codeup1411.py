a,b = map(int,input().split())
li = []
sum = 0
for i in range(a,b+1):
    for j in range(i):
        li.append(i)

for i in range(a,b):
    sum += li[i-1]
print(sum)