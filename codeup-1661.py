a = input()
for i in a:
    if(i==','):
        print('',end=" ")
    elif(i==';'):
        print()
    elif(i==' '):
        pass
    else:
        print(i,end="")