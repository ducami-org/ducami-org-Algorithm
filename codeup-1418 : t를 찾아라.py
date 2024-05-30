arr=list(input())
count=arr.count("t")
for i in range(count):
    print((arr.index("t"))+1,end=" ")
    arr[arr.index("t")]="0"