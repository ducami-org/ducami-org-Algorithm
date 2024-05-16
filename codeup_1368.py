a, b, c = input().split()
a = int(a)
b = int(b)
if c == "L":
    for i in range(0, a):
        for j in range(i):
            print(" ",end='')
        for j in range(b):
            print("*", end='')
        print()
else:
    for i in range(0, a):
        for j in range(b):
            print("*", end='')
        for j in range(i):
            print(" ",end='')
        print()