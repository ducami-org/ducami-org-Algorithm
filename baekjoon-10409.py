a,b = map(int,input().split())
c = list(map(int,input().split()))
total =0; count=0
for i in c:
    if(total+i>b):
        break
    else:
        total += i
        count +=1
print(count)