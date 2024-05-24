n = int(input())
li = [i for i in range(1,n+1)]
cnt = 0
for i in range(1,len(li)+1):
    if i == 1:
        cnt += 1
    elif i%10==1:
        cnt+=1
print(cnt)