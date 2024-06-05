a = int(input())
for i in range(a):
    count = a*(i+1)
    for j in range(a):
        print(count,end=" ")
        count-=1
    print()