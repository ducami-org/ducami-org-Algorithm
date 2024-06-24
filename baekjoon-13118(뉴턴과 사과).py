arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=0
if arr2[0] in arr1:
    print(arr1.index(arr2[0])+1)
else:
    print(0)