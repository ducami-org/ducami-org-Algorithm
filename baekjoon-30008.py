a,b = map(int,input().split())
d = list(map(int,input().split()))
c =list()
for i in d:
    b = (i*100)//a
    if(b<=4):
        c.append(1)
    elif(b<=11):
        c.append(2)
    elif(b<=23):
        c.append(3)
    elif(b<=40):
        c.append(4)
    elif(b<=60):
        c.append(5)
    elif(b<=77):
        c.append(6)
    elif(b<=89):
        c.append(7)
    elif(b<=96):
        c.append(8)
    else:
        c.append(9)
        
for i in c:
    print(i,end=" ")