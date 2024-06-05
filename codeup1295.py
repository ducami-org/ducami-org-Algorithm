a = input()
for i in range(len(a)):
    if ord(a[i]) < 97:
        print(a[i].lower(),end='')
    else:
        print(a[i].upper(),end='')
