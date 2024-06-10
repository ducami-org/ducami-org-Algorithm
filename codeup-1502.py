a = int(input())
count=1
for i in range(a):
    for j in range(a):
        print(count,end=" ")
        count+=a
    print()
    count=i+2