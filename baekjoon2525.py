a,b = map(int,input().split())
t = int(input())
sum = a * 60 + b + t
if sum//60 >= 24:
    sum -= 24 * 60
    print(f"{sum//60} {sum%60}")
else:
    print(f"{sum//60} {sum%60}")
