a,b=map(int,input().split())
arr=[[0 for i in range(b)]for j in range(a)]
c=a*b
for i in range(a):
    for j in range(b):
        arr[i][j]=c
        c-=1

for i in range(a):
    for j in range(b):
        print(arr[i][j],end=" ")
    print()