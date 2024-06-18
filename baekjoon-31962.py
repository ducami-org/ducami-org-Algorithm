a,b = map(int,input().split())
count=-1
for i in range(a):
    x,y = map(int,input().split())
    if(x+y<=b and count<x):
        count = x
print(count)