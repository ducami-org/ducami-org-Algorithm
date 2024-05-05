a,b,c=map(int,input().split())

d=a+b+c
l=list(map(int,str(d)))

if(int(l[-3])%2==0):
    print("대박")
else:
    print("그럭저럭")