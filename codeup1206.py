a,b =map(int,input().split())
cnt = 0
for i in range(1,a+1):
    if b%a==0 and a*i==b:
        print(f"{a}*{i}={b}")
        cnt += 1
        break
    elif a%b == 0 and b*a==a:
        print(f"{b}*{i}={a}")
        cnt += 1
        break
if cnt <= 0:
    print('none')