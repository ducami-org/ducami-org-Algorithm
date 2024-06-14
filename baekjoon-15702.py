record=[0]
n,m = map(int,input().split())
score = list(map(int,input().split()))
sum =0
num=100001

for i in range(m):
    tmp = list(input().split())
    cnt =0
    for j in range(1,n+1):
        if(tmp[j]=='O'):
            cnt += int(score[j-1])
            
    if(sum<cnt):
        sum=cnt
        num=int(tmp[0])
    elif(sum==cnt):
        num = min(num,int(tmp[0]))
print(num,sum)