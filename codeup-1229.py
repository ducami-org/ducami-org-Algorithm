a,b = map(float,input().split())
if(a<150):
    avg=a-100
elif(a<160):
    avg=(a-150)//2 + 50
else:
    avg=(a-100)*0.9

bimando = ((b-avg)*100)//avg

if(bimando<=10):
    print('정상')
elif(bimando<=20):
    print('과체중')
else:
    print('비만')
print(bimando)