n=int(input())
dic={}
for i in range(n):
    a,b=map(int,input().split())
    dic[a]=b

a=sorted(dic)
for i in a:
    print(i,dic[i])