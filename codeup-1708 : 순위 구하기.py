n=int(input())
arr=list(map(int,input().split()))

for i in range(n):
    count=1
    for j in range(n):
        if i==j:
            pass
        elif arr[i]<arr[j]:
            count+=1
    print(arr[i],count)



