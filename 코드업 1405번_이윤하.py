n=int(input())
l=list(input().split())
for i in l:
    print(i,end=' ')
print()
for i in range(n-1):
    a=l.pop(0)
    l.append(a)
    for j in l:
        print(j,end=' ')
    print()

