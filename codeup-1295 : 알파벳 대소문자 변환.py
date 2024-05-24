a=list(input())
for i in range(len(a)):
    if ord(a[i]) >=65 and ord(a[i])<=90:
        a[i]=chr(ord(a[i])+32)
    elif ord(a[i]) >=97 and ord(a[i])<=122:
        a[i]=chr(ord(a[i])-32)
for i in range(len(a)):
    print(a[i],end="")