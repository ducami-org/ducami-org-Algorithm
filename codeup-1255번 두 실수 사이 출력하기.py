from sys import stdin
a,b = map(float, stdin.readline().split())

while a<=b:
    print('%.2f' %a,end=' ')
    a+=0.01