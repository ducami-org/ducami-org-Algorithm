a = int(input())
d = list(map(int,input().split()))
if(d[0]>=d[1]):
    check=10
    for i in range(a-1):
        if(d[i]<d[i+1]):
            check+=1
            print('섞임')
            break
else:
    check=12
    for i in range(a-1):
        if(d[i]>d[i+1]):
            check+=1
            print('섞임')
            break
        
if(check==12):
    print('오름차순')
elif(check==10):
    print('내림차순')
