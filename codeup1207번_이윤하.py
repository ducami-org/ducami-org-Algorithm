l=map(int,input().split())
sum=0
for i in l:
    if i==1:
        sum+=1

if sum==1:
    print('도')
elif sum==2:
    print('개')
elif sum==3:
    print('걸')
elif sum==4:
    print('윷')
else:
    print('모')

