a,b,c=map(int,input().split(" "))
count=0
for i in range(1,c+1):
    if a%i==0 and b%i==0 and c%i==0 :
        count=i
print(count)