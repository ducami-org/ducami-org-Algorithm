for i in range(int(input())):
    a,b,c,min1 = map(int,input().split())
    d= [a,b,c]
    if(min(d)!=min1):
        print(i+1, min(d))
        exit()
print(-1)