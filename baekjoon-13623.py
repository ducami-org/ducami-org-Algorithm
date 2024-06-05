a,b,c = map(int,input().split())
d=[a,b,c];count=0
if(a==b==c):
    print('*')
elif(d.count(0)>d.count(1)):
    count = d.index(1)+1
else:
    count = d.index(0)+1

if(count==1):
    print('A')
elif(count==2):
    print('B')
elif(count==3):
    print('C')