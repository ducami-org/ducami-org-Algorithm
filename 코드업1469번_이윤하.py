n=int(input())
for i in range(n):
    if i%2!=0:
        for j in range(1+i*n,n*(i+1)+1):
            print(j,end=' ')
        print()
    else:
        for j in range(n*(i+1),n*i,-1):
            print(j,end=' ')
        print()