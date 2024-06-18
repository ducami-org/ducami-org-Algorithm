i=list(map(int,input().split()))
a=list(map(int,input().split()))
s=0
t=0
for j in i:
    s+=j
for i in a:
    t+=i

print(max(s,t))