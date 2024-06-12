a = list(input())
happy=0
sad=0
for i in range(len(a)-2):
    if(a[i]==':' and a[i+1]=='-' and a[i+2]==')'):
        happy+=1
    elif(a[i]==':' and a[i+1]=='-' and a[i+2]=='('):
        sad+=1
        
if(happy==sad==0):
    print('none')
elif(happy==sad):
    print('unsure')
elif(happy>sad):
    print('happy')
else:
    print('sad')