n=int(input())
for i in range(1,n+1):
    print((i-1)*' '+(n*2-(i*2-1))*'*',end='')
    print()