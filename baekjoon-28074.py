a  = input()
M =0; O=0; I=0; B=0; S=0
for i in a:
    if(i=='M'):
        M+=1
    elif(i=='O'):
        O+=1
    elif(i=='B'):
        B+=1
    elif(i=='S'):
        S+=1
    elif(i=='I'):
        I+=1
        
if(M>=1 and O>=1 and I>=1 and B>=1 and S>=1):
    print('YES')
else:
    print('NO')