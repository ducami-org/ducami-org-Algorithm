n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))

a = int(input())
for i in range(1,a):
    print(' '*(a-i) + '*'*(2*i-1))
for i in range(a,0,-1):
    print(' '*(a-i) + '*'*(2*i-1))