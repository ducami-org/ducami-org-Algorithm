n = int(input())
n = list(str(n))

if len(n) == 4:
    print(int(n[0])*10 + int(n[1]) + int(n[2])*10 + int(n[-1]))
elif len(n) == 3:
    print(int(n[0])*10 + int(n[1]) + int(n[-1]))
elif len(n) == 2:
    print(int(n[0])+int(n[1]))