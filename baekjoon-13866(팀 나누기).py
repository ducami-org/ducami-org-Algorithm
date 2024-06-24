arr=list(map(int,input().split()))
arr.sort(reverse=True)
if (arr[0]+arr[3])>=(arr[1]+arr[2]):
    print((arr[0]+arr[3])-(arr[1]+arr[2]))
else:
    print((arr[1]+arr[2])-(arr[0]+arr[3]))