for i in range(int(input())):
    a = list(input())
    for i in a[0]:
        print(i.upper(),end="")
    a.remove(a[0])
    for i in a:
        print(i,end="")
    print()