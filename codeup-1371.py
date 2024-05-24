a = int(input())
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    print("*",end="")
    for j in range(i*2):
        print(" ",end="")
    print("*")
for i in range(a):
    for j in range(i):
        print(" ",end="")
    print("*",end="")
    for j in range((a-i-1)*2):
        print(" ",end="")
    print("*")