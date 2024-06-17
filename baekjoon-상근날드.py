arr=[0]*5
for i in range(5):
    arr[i]=int(input())
print(min(arr[0],arr[1],arr[2])+min(arr[3],arr[4])-50)