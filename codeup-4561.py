d=[];min=101;total=0
for i in range(7):
   d.append(int(input()))

for i in d:
    if(i%2==1):
        if(min>i):
            min = i
        total +=i

if(min==101):
    print(-1)
else:
    print(total,min ,sep="\n")
