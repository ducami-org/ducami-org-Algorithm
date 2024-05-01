#내가 제출한 정답
a,b = map(int,input().split())
c = [0] * a
c = list(map(int,input().split()))
for i in range(0,a):
    if c[i] < b:
        print(c[i],end=' ')
#다른 답안
n,x = map(int,input().split())
num = list(map(int,input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i],end=' ')