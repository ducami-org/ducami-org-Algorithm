n = int(input())
yaksu = []
for i in range(1,n+1):
    if n%i==0:
        yaksu.append(i)
for i in yaksu:
    print(i,end=' ')