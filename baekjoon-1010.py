a = int(input())
for i in range(a):
    a,b = map(int,input().split())
    d=1; e=1;f=1
    for i in range(1,b+1):
        d *= i

    for i in range(1,b-a+1):
        e *= i

    for i in range(1,a+1):
        f *= i
        
    print(d//(e*f))