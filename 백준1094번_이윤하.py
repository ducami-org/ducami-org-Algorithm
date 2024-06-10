n=int(input())
l=[64,32,16,8,4,2,1]
cnt=0
for i in range(len(l)):
    if n >= l[i]:
        cnt+=1
        n-=l[i]
    if n==0:
        break
print(cnt)


