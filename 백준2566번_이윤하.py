arr1=[]
for i in range(9):
    arr1.append(list(map(int,input().split())))
    
        
    
m=[]
for i in arr1:
    m.append(max(i))
print(max(m))

for i in arr1:
    if max(m) in i:
        print(arr1.index(i)+1,i.index(max(m))+1)
        

