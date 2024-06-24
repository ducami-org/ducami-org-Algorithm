while True:
    arr=input()
    if arr=="END":
        break
    else:
        arr=list(arr)
        arr.reverse()
        for i in arr:
            print(i,end="")