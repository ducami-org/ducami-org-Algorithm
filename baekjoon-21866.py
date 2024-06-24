a = list(map(int,input().split()))
d=[100,100,200,200,300,300,400,400,500]
for i in range(len(d)):
    if(a[i]>d[i]):
        print('hacker')
        exit()
if(sum(a)>=100):
    print('draw')
else:
    print('none')