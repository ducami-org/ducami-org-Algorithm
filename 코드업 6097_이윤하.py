h,w=map(int,input().split())
n=int(input())
arr=[[0 for i in range(w)] for j in range(h)]

for i in range(n):
    l,d,x,y=map(int,input().split())
    if d==0:
        for j in range(y-1,y+l-1):
            arr[x-1][j]=1
    else:
        for j in range(x-1,x+l-1):
            arr[j][y-1]=1
for i in range(h):
    for j in range(w):
        print(arr[i][j],end=' ')
    print()
        
            
            
