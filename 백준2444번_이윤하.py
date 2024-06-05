n=int(input())
for i in range(1,n+1):
    print((n-i)*' '+(i*2-1)*'*',end='')
    print()
for j in range(1,n):
    print(j*' '+((n-1)*2-(j*2-1))*'*',end='')
    print()