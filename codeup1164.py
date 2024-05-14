a,b,c = map(int,input().split())
cr = 0
for i in range(3):
    if a <= 170 or b <= 170 or c <= 170:
        cr += 1
if cr > 0:
    print('CRASH')
else:
    print('PASS')