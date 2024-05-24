# baekjoon1712 손익분기점

a,b,c = map(int,input().split())
if b >= c:
    print(-1)
else:
    c-=b
    print(a//c+1)