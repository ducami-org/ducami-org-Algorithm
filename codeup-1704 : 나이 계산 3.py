arr=list(map(str,input().split()))

if int(arr[1][0]) == 1 :
    print(2012-(int(arr[0][:2])+1899),end=" ")
    print("M")
elif int(arr[1][0]) == 2 :
    print(2012-(int(arr[0][:2])+1899),end=" ")
    print("F")
elif int(arr[1][0]) == 3 :
    print(2012-(int(arr[0][:2])+1999),end=" ")
    print("M")
elif int(arr[1][0]) == 4 :
    print(2012-(int(arr[0][:2])+1999),end=" ")
    print("F")
