a = int(input())
for i in range(a):
    b = int(input())
    P1=0; P2=0
    for j in range(b):
        x,y = input().split()
        if((x=='R' and y=='S') or (x == 'P' and y=='R') or (x=='S' and y=='P')):
            P1+=1
        elif((x=='S' and y=='R') or (x == 'R' and y=='P') or (x=='P' and y=='S')):
            P2+=1
    if(P1>P2):
        print('Player 1')
    elif(P1<P2):
        print('Player 2')
    else:
        print('TIE')