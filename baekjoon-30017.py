a,b = map(int,input().split())
total =1
a-=1
while True:
    if(a<1 or b<1):
        print(total)
        break
    total +=2
    a-=1
    b-=1