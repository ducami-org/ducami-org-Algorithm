a = int(input())
num=1
for i in range(a//2+1):
    for j in range((a//2)-i):
        print(" ",end="")
    print("*"*num)
    num+=2
