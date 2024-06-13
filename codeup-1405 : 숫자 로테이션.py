n=int(input())
arr=[]
arr=list(map(int,input().split()))
for i in range(n):
    for j in range(0+i,n+i):
        count=j
        if count >= n:
            count-=n
        print(arr[count],end=" ")
    print()