a = int(input())
if(a==1):
    print(int(input()))
else:
    b =list(map(int,input().split()))
    b.sort(reverse=True)
    print(b[0])