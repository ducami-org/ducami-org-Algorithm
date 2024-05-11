a = list(map(int,input().split()))
total=0
for i in a:
    if(i%5==0):
        total =i
        break
    
print(total)