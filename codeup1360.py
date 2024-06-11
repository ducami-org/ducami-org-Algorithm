n = int(input())
dkan = n
for i in range(n,0,-1):
    for j in range(i):
        print(dkan,end=' ')
    dkan-= 1
    print()