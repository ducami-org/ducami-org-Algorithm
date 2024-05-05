n=int(input())
max=0
sum=0
for i in range(n):
    a,b,c=map(int,input().split())
    if a==b==c:
        sum=10000+a*1000
    elif a==b or a==c:
        sum=1000+a*100
    elif b==c:
        sum=1000+b*100
    else:
        if a>b and a>c:
            sum=a*100
        elif b>a and b>c:
            sum=b*100
        else:
            sum=c*100
    
    if max<sum:
        max=sum
print(max)

