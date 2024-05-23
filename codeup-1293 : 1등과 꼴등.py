n=int(input())
l_max=[]
l_min=[]
m=list(map(int,input().split()))
for i in range(n):
    l_max.append(m[i])
    l_min.append(m[i])
print(max(l_max),min(l_min))