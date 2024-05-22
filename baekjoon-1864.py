while True:
    a = list(input())
    total=0; count = len(a)-1
    if(a[0]=='#'):
        break
    for i in a:
        if(i=='\\'):
            total += (8**count)
        elif(i=='('):
            total += 2*(8**count)
        elif(i=='@'):
            total += 3*(8**count)
        elif(i=='?'):
            total += 4*(8**count) 
        elif(i=='>'):
            total += 5*(8**count)
        elif(i=='&'):
            total += 6*(8**count) 
        elif(i=='%'):
            total += 7*(8**count) 
        elif(i=='/'):
            total += -1*(8**count)
        count -=1
    print(total)