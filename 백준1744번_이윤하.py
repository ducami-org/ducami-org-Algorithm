w=input()
for i in w:
    if ord(i)>90:
        print(chr(ord(i)-32),end='')

    else:
        print(chr(ord(i)+32),end='')