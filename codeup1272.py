a,b = map(int,input().split())
arr = []
if a>b:
    for i in range(1,a):
        arr.append(i)
        arr.append(i*10)    
else:
    for i in range(1,b):
        arr.append(i)
        arr.append(i*10)    
print(arr[a-1] + arr[b-1])