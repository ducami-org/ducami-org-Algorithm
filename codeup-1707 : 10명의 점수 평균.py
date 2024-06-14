arr=[]
arr=list(map(int,input().split()))
tot=sum(arr)/10

up=0
down=0

for i in arr:
    if i >=tot:
        up+=1
    else:
        down+=1
print(f"{tot:.1f}")
print(f"{up} {down}")