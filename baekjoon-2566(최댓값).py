# arr=[0,2,1,2,1,4]
# print(arr.index(max(arr))) 0 5

index1=0
index2=0
arr_l=[0]
arr_in=[]
ma=0
for i in range(9):
    arr_in=list(map(int,input().split()))
    if max(arr_in) > ma:
        ma=max(arr_in)
        index1=i+1
        index2=arr_in.index(ma)+1
        
print(ma)
print(index1,index2)