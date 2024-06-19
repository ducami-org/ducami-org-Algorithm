arr=[]
for i in range(4):
    arr.append(int(input()))
tot=sum(arr)
print(tot//60)
print(tot%60)