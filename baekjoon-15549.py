while True:
    a = input()
    count=0;total =0
    if(a=='0'):
        break
    for i in a:
        if(i=='0'):
            total+=4
        elif(i=='1'):
            total+=2
        else:
            total +=3
        count +=1
    total+=count+1
    print(total)