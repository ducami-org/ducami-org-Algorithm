l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
cnt = 0
while cnt == 0:
    a -= c
    b -= d
    if a <= 0 and b <= 0:
        print(l-1)
        break
    l -= 1