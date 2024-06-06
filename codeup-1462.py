a = int(input())
count=1
for i in range(a):
    for j in range(a):
        print(count+(j*a),end=" ")
    count+=1
    print()