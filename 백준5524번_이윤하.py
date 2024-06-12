n=int(input())
for i in range(n):
    w=input()
    for j in w:
        if ord(j)<90:
            print(chr(ord(j)+32),end='')
        else:
            print(j,end='')
    print()