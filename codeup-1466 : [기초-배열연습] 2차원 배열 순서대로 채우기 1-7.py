a,b=map(int,input().split())
for i in range(a):
    for j in range(0,a*b,a):
        print(a*b-i-j,end=" ")
    print()