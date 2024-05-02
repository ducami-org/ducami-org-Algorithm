h,w=map(float,input().split())
a=(h-100)*0.9
b=(w-a)*100/a
if b<=10:
    print('정상')
elif b>10 and b<=20:
    print('과체중')
    
else:
    print('비만')