a = int(input())
hour = 1
time=0
for i in range(a):
    b,c = input().split()
    check='NO'
    if(int(c)==hour):
        check='YES'
    if(b=='CLOCK' or b=='WATCH'):
        print(hour, check)
    elif(b=='HOURGLASS' and check=='YES'):
        print(hour,'NO')
    else:
        if(time==0):
            time=1
        else:
            time=0  
        print(hour, check)
        
    if(time==0):
        hour+=1
        if(hour>12):
            hour = hour%12
    else:
        hour-=1
        if(hour<=0):
            hour+=12