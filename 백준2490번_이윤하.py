
for i in range(3):
    sum=0
    a=list(map(int,input().split()))
    
    for j in a:
        if j==0:
            sum+=1
    if sum==1:
        print('A')
    elif sum==2:
        print('B')
    elif sum==3:
        print('C')
    elif sum==4:
        print('D')
    else:
        print('E')
