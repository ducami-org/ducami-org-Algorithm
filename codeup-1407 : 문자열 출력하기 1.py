arr=list(input())
count=arr.count(" ")
for i in range(count):
    arr.remove(" ")
for i in arr:
    print(i,end="")