n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=input()
arr.sort()
for i  in range(n):
    print(arr[i])