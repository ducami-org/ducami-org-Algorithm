n=list(map(int,input().split()))
a=0
b=0
for i in n:
    if i%5!=0:
        a+=1

    if a>=10:
        print(0)

    if i%5==0:
        b+=1
        print(i)
        if b>=1:
            break