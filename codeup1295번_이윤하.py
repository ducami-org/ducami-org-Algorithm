l=input()
a=[]
for i in l:
    if ord(i)>90:

        a.append(chr(ord(i)-32))
    elif ord(i)<60:
        a.append(i)
    else:
        a.append(chr(ord(i)+32))
for i in a:
    print(i,end='')