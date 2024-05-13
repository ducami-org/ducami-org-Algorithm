a = input()
a = list(a)
for i in range(len(a)):
    if ord(a[i]) >= 65 and ord(a[i]) <= 90:
        print(chr(ord(a[i])+32), end='')
    elif ord(a[i]) >= 97 and ord(a[i]) <= 122:
        print(chr(ord(a[i])-32), end='')
    else:
        print(a[i], end='')