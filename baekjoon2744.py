n = input()
for i in range(len(n)):
    if 97 <= ord(n[i]) <= 122:
        print(n[i].upper(),end='')
    else:
        print(n[i].lower(),end='')
