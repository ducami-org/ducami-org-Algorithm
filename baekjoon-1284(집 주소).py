while True:
    tot=0
    n=input()
    if int(n)==0:
        break
    for i in n:
        if int(i)==1:
            tot+=2
        elif int(i)==0:
            tot+=4
        else: 
            tot+=3
        tot+=1
    print(tot+1)