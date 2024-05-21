d = [chr(i) for i in range(97, 123)]
a = input()
for i in a:
    if(i==' '):
        print('',end=" ")
    else:
        if(i=='z'):
            print('c',end="")
        elif(i=='y'):
            print('b',end="")
        elif(i=='x'):
            print('a',end="")
        else:
            print(d[(ord(i)+3)%97],end="")