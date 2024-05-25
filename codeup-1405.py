a  =int(input())
b = list(map(int,input().split()))
for i in range(len(b)):
    for j in b:
        print(j,end=" ")
    temp = b[0]
    b.remove(temp)
    b.append(temp)
    print()