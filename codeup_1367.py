a = int(input())
for i in range(a-1, -1, -1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, a):
        print('*', end='')
    print()