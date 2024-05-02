n=int(input())
m=[[0]*n]*n
c=1
for i in range(n):
    for j in range(n):
        print(c,end=" ")
        c=c+1
    print()