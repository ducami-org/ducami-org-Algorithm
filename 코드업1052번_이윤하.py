n=int(input())

for i in range(1,n+1):
    sum=i
    for j in range(n):
        print(sum,end=' ')
        sum+=n
    print()
