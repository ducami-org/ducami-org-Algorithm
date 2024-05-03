
max=0
for i in range(3):
    a,b=map(int,input().split())
    if max<a*b:
        max=a*b
print(max)