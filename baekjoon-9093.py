a = int(input())
for i in range(a):
    b = list(input().split())
    for i in b:
       i = ''.join(reversed(i))
       print(i,end=" ")
    print()