for i in range(3):
    tot=[0]*3
    arr=list(map(int,input().split()))
    tot[0]=arr[3]-arr[0]
    tot[1]=arr[4]-arr[1]
    tot[2]=arr[5]-arr[2]
    if tot[2]<0:
        tot[1]-=1
        tot[2]+=60
    if tot[1]<0:
        tot[0]-=1
        tot[1]+=60
    print(*tot)