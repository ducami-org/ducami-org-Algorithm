a,b = map(int,input().split())
for i in range(a):
    c = list(input())
    for i in range(b):
        if(c[i]!='.'):
            c[-i-1]=c[i]
    for i in c:
        print(i,end="")
    print()