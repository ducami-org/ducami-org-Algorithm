# in 앞이 뒤에 있는가?

n=int(input())
count=0
arr=[0 for i in range(n)]

for i in range(n):
    arr[i]=input()

for i in range(n):
    if len(arr[i])<=3 or ("tap" in arr[i]) or ("xocure" in arr[i]):
        print(arr[i])
        count+=1
if count<=3:
    print("safe")
elif count<=6:
    print("warning")
else:
    print("danger")