def b(q, sum):
    if sum in q:
        print(q.index(sum)+1)
    else:
        print(-1)
n = int(input())
a = list(map(int, input().split()))
k = int(input())
b(a, k)