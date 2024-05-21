a = int(input())
for i in range(a):
    b = list(input().split())
    total = float(b[0])
    del b[0]
    for j in b:
        if(j=='@'):
            total*=3
        elif(j=='%'):
            total +=5
        else:
            total -=7
    print(f"{total:.2f}")