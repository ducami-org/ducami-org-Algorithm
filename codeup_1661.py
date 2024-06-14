def sum(a):
    for i in range(len(a)):
        if a[i] == ',':
            print(" ",end='')
        elif a[i] == ';':
            print()
        elif a[i] == " ":
            continue
        else:
            print(a[i], end='')
    print()
a = input()
sum(a)