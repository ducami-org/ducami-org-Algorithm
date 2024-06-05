def num(a,b):
    if a>b:
        return
    else:
        if a%2!=0:
            print(a,end=' ')
        num(a+1,b)


a,b=map(int,input().split())
num(a,b)