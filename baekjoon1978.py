n = int(input())
arr = list(map(int, input().split()))

sosu = 0
for i in arr:
    if i==1:
        continue
    else:
        yaksu = 0
        for j in range(2, i):
            if i%j==0:
                yaksu += 1
        if yaksu == 0:
            sosu += 1
print(sosu)