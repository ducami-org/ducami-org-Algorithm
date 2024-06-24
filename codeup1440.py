a,b= map(int,input().split())
li = list(map(int,input().split()))
li2 = list(map(int,input().split()))
for i in range(len(li2)):
    li.append(li2[i])
li.sort()
for i in li:
    print(i,end=' ')