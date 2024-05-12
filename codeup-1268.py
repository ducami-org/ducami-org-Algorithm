a =int(input())
b = list(map(int,input().split()))
count =0
for i in b:
    if(i%2==1):
        count +=1
        
print(count)