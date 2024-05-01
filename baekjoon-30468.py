a,b,c,d,e = map(int,input().split())
avg = (a+b+c+d)//4
total =0
while True:
    if(avg<e):
        total +=1
        a +=1
        avg = (a+b+c+d)//4
    else:
        print(total)
        break