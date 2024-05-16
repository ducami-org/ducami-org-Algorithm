a = list(map(int,input().split()))
cnt = False
if a[len(a)-1]<10:
    cnt = True
for i in range(len(a)):
    print(a[i],end='')
    if cnt == True and i == len(a)-2:
        print(0,end='')
        cnt = False