a,b,c = map(int,input().split())
d = int(input())
temp = a * 3600 + b * 60 + c + d
if temp // 3600 >24:
    print(f"{temp//3600-25} {temp%3600//60} {temp%60}")

elif  temp // 3600 == 24:
    temp -= a*3600
    print(f"{temp//3600-1} {temp%3600//60} {temp%60}")

else:
    print(f"{temp//3600} {temp%3600//60} {temp%60}")
