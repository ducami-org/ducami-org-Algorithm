while True:
    check=0
    high=[]
    low=[]
    while True:
        a = int(input())
        if(a==0):
            check+=1
            break
        b = input()
        if(b=='right on'):
            break
        elif(b=='too high'):
            high.append(a)
        else:
            low.append(a)
    if(check==1):
        break
    for i in high:
        if(a>=i):
            print('Stan is dishonest')
            check+=1
            break
    if(check==0):
        for i in low:
            if(a<=i):
                print('Stan is dishonest')
                check+=1
                break
    if(check==0):
        print('Stan may be honest')