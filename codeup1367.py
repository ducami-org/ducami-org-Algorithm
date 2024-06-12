n = int(input())

for i in range(n,0,-1):
    for j in range(i-1):
        print(' ',end='')
    for j in range(n):
        print('*',end='')
    print()