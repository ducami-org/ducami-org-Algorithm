import math
import sys
while True:
    total=0
    a = list(sys.stdin.readline().rstrip())
    if(a[0]=='0'):
        break
    else:
        for i in range(len(a)):
            total += int(a[i])*math.factorial(len(a)-i)
    print(total)