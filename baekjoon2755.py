import math
n = int(input())
sum = 0
avg = 0
for i in range(n):
    a,b,c = input().split()
    b = int(b)
    avg += b
    if c=='A+':
        sum += b *4.3
    elif c=='A0':
        sum += b * 4.0
    elif c=="A-":
        sum += b * 3.7
    elif c=='B+':
        sum += b * 3.3
    elif c=='B0':
        sum += b * 3.0
    elif c=='B-':
        sum += b * 2.7
    elif c=='C+':
        sum += b * 2.3
    elif c=='C0':
        sum += b * 2.0
    elif c=='C-':
        sum += b * 1.7
    elif c=='D+':
        sum += b * 1.3
    elif c=='D0':
        sum += b * 1.0
    elif c=='D-':
        sum += b * 0.7
    else:
        sum += b * 0




