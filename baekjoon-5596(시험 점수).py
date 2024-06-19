arr=[]
for i in range(2):
    arr.append(list(map(int,input().split())))
if sum(arr[0])>sum(arr[1]):
    print(sum(arr[0]))
else:
    print(sum(arr[1]))