h,k,d = input().split()

if d == 'L':
    for i in range(int(h)):
        for j in range(i):
            print(' ',end='')
        for j in range(int(k)):
            print('*',end='')
        print()

else:
    for i in range(int(h)-1, -1, -1):
        for j in range(0, i):
            print(' ', end='')
        for j in range(0, int(k)):
            print('*', end='')
        print()