w=input()
a=[]
b=[]
for i in w:
    a.append(chr(ord(i)+2))
    b.append(chr((ord(i)*7)%80+48))
for i in a:
    print(i,end='')
print()
for i in b:
    print(i,end='')

    
