n=int(input())
li=[]
c=0
for i in range(n):
    li=list(map(int,input().split()))
    if min(li[:-1]) == li[3]:
        pass
    elif min(li[:-1]):
        print(i+1,min(li[:-1]))
        c=1
        break
        
if c==0:
    print("-1")