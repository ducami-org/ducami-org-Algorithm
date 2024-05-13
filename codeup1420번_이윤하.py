n=int(input())
l=[]
dic={}
for i in range(n):
    a,b=input().split()
    l.append(int(b))
    dic[a]=int(b)


t=sorted(l)[n//2]

if t in dic.values():
    for key,value in dic.items():
        if value ==t:
            print(key)
            break




