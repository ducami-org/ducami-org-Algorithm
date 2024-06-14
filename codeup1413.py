li = list(input().split())
result = []
for i in range(len(li)-1,-1,-1):
    for j in range(len(li[i])-1,-1,-1):
        print(li[i][j],end='')
    print(' ',end='')


