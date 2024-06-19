a,b = map(int,input().split())
name={}
for i in range(a):
    c,d = input().split()
    name[c]=d
for j in range(b):
    print(name[input()])