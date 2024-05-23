a = int(input())
num=0
for i in range(1,a+1):
    num += i
for i in range(a):
    for j in range(i+1):
        print(num,end=" ")
        num-=1
    print()