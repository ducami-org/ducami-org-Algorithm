a = input()
a = int(a)

b = 2012 - a + 1

if(b < 2000):
    b = str(b)
    print(int(b[2:4]), 1)
else:
    b = str(b)
    print(int(b[2:4]), 3)