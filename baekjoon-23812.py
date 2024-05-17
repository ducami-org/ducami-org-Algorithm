a = int(input())
for i in range(2):
    for j in range(a):
        print("@"*a,end="")
        print(" "*(a*3),end="")
        print("@"*a)
    for j in range(a):
        print("@"*(a*5))
for i in range(a):
    print("@"*a,end="")
    print(" "*(a*3),end="")
    print("@"*a)
        