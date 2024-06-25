n = int(input())
start = 0
end = 0 
for i in range(n,n**2+1,n):
    start  += n
    for j in range(start,end,-1):
        print(j,end=' ')
    end = start
    print()
    