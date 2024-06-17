def f(a,b,c):
    l=[a,b,c]
    l.remove(max(l))
    l.remove(min(l))
    for i in l:
        return i
a,b,c=map(int,input().split())
print(f(a,b,c))