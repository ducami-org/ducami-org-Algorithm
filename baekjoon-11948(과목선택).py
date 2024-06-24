arr=[0]*6
for i in range(6):
    arr[i]=int(input()) 
arr1=arr[0:4]
arr1.sort(reverse=True)
arr2=arr[4:]
arr2.sort(reverse=True)
print(sum(arr1[0:3])+arr2[0])
