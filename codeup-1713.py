a,b = map(int,input().split())
total=0
for i in range(a,b+1):
    if(i%3==0 and i%4!=0):
        total +=i
    if(i%4==0 and i%3!=0):
        total -=i
print(total)