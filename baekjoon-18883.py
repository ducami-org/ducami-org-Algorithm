a,b = map(int,input().split())
count=0
for i in range(a*b):
    count+=1
    if(count==b):
        print(i+1)
        count=0
    else:
        print(i+1,end=" ")