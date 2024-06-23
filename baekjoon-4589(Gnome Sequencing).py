n=int(input())
arr_s=[]
for i in range(n):
    arr=list(map(int,input().split()))
    arr1=arr.copy()
    arr1.sort()
    arr2=arr.copy()
    arr2.sort(reverse=True)
    if arr==arr1 or arr==arr2:
        arr_s.append("Ordered")
    else:
        arr_s.append("Unordered")
print("Gnomes:")
for i in range(n):
    print(arr_s[i])

        