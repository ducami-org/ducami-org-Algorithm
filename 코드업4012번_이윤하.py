n=int(input())
l=list(map(int,input().split()))

for i in l:
    sum=0
    for j in l:
        if i>=j:
            sum+=1

    print(i,n-(sum-1))
