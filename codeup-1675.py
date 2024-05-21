d = [chr(i) for i in range(97, 123)]
a = input()
for i in a:
    if(i==' '):
        print('',end=" ")
    else:
        print(d[ord(i)%97-3],end="")