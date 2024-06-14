for i in range(int(input())):
    a,b = input().split()
    a2=0
    a = a[::-1]
    b = b[::-1]
    for i in range(len(a)):
        if(a[i]=='1'):
            a2 += 2**i
    for i in range(len(b)):
        if(b[i]=='1'):
            a2 += 2**i
    a2= bin(a2)
    print(a2[2:])