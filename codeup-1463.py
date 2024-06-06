a = int(input())
count=a
for i in range(a):
    for j in range(a):
        print(count+(a*j),end=" ")
    print()
    count-=1