n=int(input())
def num():
    l=list(map(int,input().split()))
    max=0
    for i in l:
        if max<i:
            max=i
    print(l.index(max)+1)
        
num()
