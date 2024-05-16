a,b = map(int,input().split())
sum = a*60 + b - 30
if sum//60 > 24:
    print(f"{sum//60-24} {sum%60}")
elif sum//60 < 0:
    print(f"{sum//60+24} {sum%60}")
else:
    print(f"{sum//60} {sum%60}")
