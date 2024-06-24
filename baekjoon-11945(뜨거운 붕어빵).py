n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr=list(input())
    arr.reverse()
    for i in range(m):
        print(arr[i],end="")
    print("")
