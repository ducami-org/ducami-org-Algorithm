a=int(input())
arr=[[0 for i in range(a)]for j in range(a)]
c=1
for i in range(a):
    for j in range(a):
        arr[i][j]=c
        c+=1
for i in range(a):
    for j in range(a):
        print(arr[i][j],end=" ")
    print()