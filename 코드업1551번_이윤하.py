n=int(input())
l=list(map(int,input().split()))
k=int(input())

def f(n,k):
    if k in l:
        print(l.index(k)+1)
    else:
        print(-1)

f(n,k)