a = list(input())
b = input()
for i in b:
    if(i==' '):
        print(' ',end="")
    else:
        print(a.index(i),end="")