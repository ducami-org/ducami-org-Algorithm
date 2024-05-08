a=int(input())
b =0 ; c=0; count=0
for i in range(a*9):
    x,y = map(int,input().split())
    b+=x
    c+=y
    count +=1
    if(count == 9):
        if(b>c):
            print('Yonsei')
        elif(b<c):
            print('Korea')
        else:
            print('Draw')
        b=0
        c=0
        count =0 