a = int(input())
print("*"*a)
for i in range(a-2):
    print("*",end="")
    print(" "*(a-2),end="")
    print("*")
print("*"*a)