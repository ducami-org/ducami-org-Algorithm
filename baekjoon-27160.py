a = int(input())
ba=0; st=0; li=0; pl=0
for i in range(a):
    b,c = input().split()
    if(b=='BANANA'):
        ba+=int(c)
    elif(b=='STRAWBERRY'):
        st+=int(c)
    elif(b=='LIME'):
        li+=int(c)
    elif(b=='PLUM'):
        pl+=int(c)
    
if(ba==5 or st==5 or li==5 or pl==5):
    print('YES')
else:
    print('NO')