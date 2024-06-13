a = list(map(int,input().split()))
count=0;count2=0
avg = sum(a)/len(a)
print(f"{avg:.1f}")
for i in a:
    if(avg>i):
        count+=1
    elif(avg<=i):
        count2+=1
        
print(count2,count)