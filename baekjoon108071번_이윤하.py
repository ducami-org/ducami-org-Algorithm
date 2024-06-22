n,m=map(int,input().split())

l=list(map(int,input().split()))
for j in l:
    if j<m:
        print(f'{j} ',end='')