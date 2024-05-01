a = int(input())
total=0
for i in range(a):
    x,y = map(int,input().split())
    if(x==68):
        if(y==136):
            total +=1000
        elif(y==142):
            total += 5000
        elif(y==148):
            total += 10000
        elif(y==154):
            total += 50000
    else:
        if(x==136):
            total +=1000
        elif(x==142):
            total += 5000
        elif(x==148):
            total += 10000
        elif(x==154):
            total += 50000
        
        
        
print(total)