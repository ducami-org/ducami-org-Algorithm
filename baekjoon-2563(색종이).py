arr=[[0]*100 for _ in range(100)]
n=int(input())
for i in range(n):
    m1,m2=map(int,input().split())
    for j in range(10):
        for k in range(10):
            try:
                arr[m1+j][m2+k]=1
            except IndexError:
                pass
tot=0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1:
            tot+=1
print(tot)
