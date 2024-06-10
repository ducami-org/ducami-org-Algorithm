h,w = map(float,input().split())
a = (h-100) * 0.9
bmi = (w-a) * 100 / a
if bmi<=10:
    print('정상')
elif 10<bmi<=20:
    print('과체중')
else:
    print('비만')