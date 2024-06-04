n = int(input())
yaksu = []
for i in range(1,n):
    if n % i == 0:
        yaksu.append(i)
print(len(yaksu))