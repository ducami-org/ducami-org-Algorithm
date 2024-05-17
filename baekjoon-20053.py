a  = int(input())
for i in range(a):
    c = int(input())
    b = list(map(int,input().split()))
    print(min(b), max(b))