a,b = map(float,input().split())
avg = (a-100)*0.9
bimando = (b-avg)*100 /avg
if(bimando>20):
    print('비만')
elif(bimando>10):
    print('과체중')
else:
    print('정상')