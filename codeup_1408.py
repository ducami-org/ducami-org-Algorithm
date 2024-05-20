a = input()
for i in range(len(a)):
    print(chr(ord(a[i]) + 2),end='')
print()
for i in range(len(a)):
    print(chr(ord(a[i])*7 % 80 + 48), end='')