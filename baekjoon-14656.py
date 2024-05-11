a= int(input())
b = list(map(int,input().split()))
count =0
for i in range(len(b)):
    if(b[i] == i+1):
        pass
    else:
        count +=1
        
print(count)