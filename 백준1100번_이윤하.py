arr1=[]
for i in range(8):
    arr1.append(list(input()))

sum=0
for i in range(8):
    if i%2==0:
        for j in range(8):
            if j%2==0 and arr1[i][j]=='F':
                sum+=1
    else:
        for j in range(8):
            if j%2!=0 and arr1[i][j]=='F':
                sum+=1

print(sum)

