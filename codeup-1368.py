a,b,c = input().split()
a=  int(a)
b=  int(b)
if(c=='L'):
    for i in range(a):
        for j in range(i):
            print(" ",end="")
        print("*"*b)
else:
    for i in range(a):
        for j in range(a-i-1):
            print(" ",end="")
        print("*"*b)