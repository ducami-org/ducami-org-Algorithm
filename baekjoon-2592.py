d=[]
e=[0 for _ in range(100)]
for i in range(10):
    a= int(input())
    d.append(a)
    e[a//10]+=1
print(sum(d)//len(d))
print(e.index(max(e))*10)