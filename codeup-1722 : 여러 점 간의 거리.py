import math
n=int(input())
li_count=[]
li=[]
tot=0.0
for i in range(n):
    li.append(list(map(int,input().split())))
for i in range(n-1):
    a=(li[i+1][0]-li[i][0])
    a=a*a
    b=(li[i+1][1]-li[i][1])
    b=b*b
    li_count.append(math.sqrt(a+b))
for i in li_count:
    tot+=i
print(f"{tot:.2f}")