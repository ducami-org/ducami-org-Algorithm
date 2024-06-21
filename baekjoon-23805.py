a = int(input())
for i in range(a):
    print("@"*(a*3),end="")
    print(" "*a,end="")
    print("@"*a)
for i in range(a*3):
    print("@"*a,end="")
    print(" "*a,end="")
    print("@"*a,end="")
    print(" "*a,end="")
    print("@"*a)
for i in range(a):
    print("@"*a,end="")
    print(" "*a,end="")
    print("@"*(a*3))
    