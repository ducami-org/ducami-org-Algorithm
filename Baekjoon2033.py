#반올림 ************* 중요

n = int(input())

start = 10
while n > start:
    temp = n  % start

    if temp >= start // 2:
        n += start
    n -= temp
    start *= 10

print(n)