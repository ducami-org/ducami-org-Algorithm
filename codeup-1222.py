a,b,c= map(int,input().split())
a = 90-a
if(a%5==0):
    b+=a//5
else:
    b+=a//5+1

if(b==c):
    print('same')
elif(b<c):
    print('lose')
else:
    print('win')