height, weight = map(int, input().split())

if height < 150:
    pm = height - 100
elif 150 <= height < 160:
    pm = 	(height - 150) /2 + 50
elif height >= 160:
    pm = (height - 100) * 0.9

if pm <= 10:
    print("정상")
elif 10 < pm <= 20:
    print("과체중")
elif pm > 20:
    print("비만")