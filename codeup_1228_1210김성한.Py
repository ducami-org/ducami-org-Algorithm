height, weight = map(float, input().split())
pyojun = (height - 100) * 0.9
biman = (weight - pyojun)  * 100 / pyojun
if biman<=10:
    print("정상")
elif biman<=20:
    print("과체중")
else:
    print("비만")