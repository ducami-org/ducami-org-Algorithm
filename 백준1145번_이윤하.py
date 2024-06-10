l=list(map(int,input().split()))
min=min(l)
while True:
    cnt=0
    for i in l:
        if min%i==0:
            cnt+=1
    if cnt>2:
        break
    min+=1
print(min)