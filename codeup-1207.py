a = list(map(int,input().split()))
total =0
for i in range(4):
    if(a[i]==0):
        total +=1
if(total ==0):
    print('윺')
elif(total==1):
    print('걸')
elif(total==2):
    print('개')
elif(total==3):
    print('도')
else:
    print('모')