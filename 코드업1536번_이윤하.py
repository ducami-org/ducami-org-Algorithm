n=int(input())
def num():
    l=list(map(int,input().split()))
    min=10000000000
    for i in l:
        if min>i:
            min=i
    return min
        
print(num())
