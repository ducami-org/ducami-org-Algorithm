a = int(input())
b=1
for i in range(a):
    for j in range(i+1):
       print(b,end=" ")
       b+=1
    print()
    b = 1 