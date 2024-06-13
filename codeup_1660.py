def sum(a):
    for i in range(len(a)):
        if a[i] == ',':
            print("", end=' ')
        else:
            print(a[i], end='')
a = input()
sum(a)