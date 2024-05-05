a,b,c,d=map(int,input().split())
sum=a
for i in range(d-1):
    sum=sum*b+c
   
print(sum)