# 키가 150 미만일 때	(실제 키 - 100)
# 키가 150이상 160미만일 때	(실제 키 - 150) /2 + 50
# 키가 160 이상일 때	(실제 키 - 100) * 0.9
# 비만도 = (실제 몸무게 - 표준몸무게)  * 100 / 표준 몸무게
h, w = map(float, input().split())
if h<150:
    pyojun = h-100
elif h<160:
        pyojun = (h-150) / 2 + 50
else:
      pyojun = (h-100) * 0.9
biman = (w-pyojun) * 100 / pyojun 
if biman<=10:
      print("정상")
elif biman<=20:
      print("과체중")
else:
      print("비만")