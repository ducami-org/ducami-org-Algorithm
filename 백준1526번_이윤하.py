n=int(input())
l=[]
for i in range(1,n+1):
    cnt=0
    word=str(i)
    for j in word:
        if j=='7':
            cnt+=1
        elif j=='4':
            cnt+=1
    if cnt==len(word):
        l.append(i)
print(max(l))


