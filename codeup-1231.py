a= input()
for i in a:
    if(i=='+'):
        b,c = a.split('+')
        print(int(b)+int(c))
    elif(i=='-'):
        b,c = a.split('-')
        print(int(b)-int(c))
    elif(i=='*'):
        b,c = a.split('*')
        print(int(b)*int(c))
    elif(i=='/'):
        b,c = a.split('/')
        print(f"{int(b)/int(c):.2f}")