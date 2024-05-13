a=int(input())
arr=[[0 for i in range(a)]for j in range(a)]

for i in range(a):
    c=(a-i)
    for j in range(a):
        arr[i][j]=c
        c+=a

for i in range(a):
    for j in range(a):
        print(arr[i][j],end=" ")
    print()