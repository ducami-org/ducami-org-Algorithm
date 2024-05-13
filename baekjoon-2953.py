a = list(map(int,input().split()))
total = sum(a)
count=1
for i in range(4):
    b=list(map(int,input().split()))
    if(total<sum(b)):
        count = i+2
        total = sum(b)
        
print(count, total)