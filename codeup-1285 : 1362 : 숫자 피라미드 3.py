n=int(input())
count=0
for i in range(n,0,-1):
    count+=i
for i in range(n,0,-1):
    for j in range(n-(i-1)):
        print(count,end=" ")
        count-=1
    print()