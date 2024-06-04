a,b = map(int,input().split())
d=list(map(int,input().split()))
count=0
d.sort()
for i in d:
    print(i,end=" ")
    count+=1
    if(count==b):
        count=0
        print()