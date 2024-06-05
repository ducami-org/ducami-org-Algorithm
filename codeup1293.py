n = int(input())
li = []
li = list(map(int,input().split()))
li.sort()
print(max(li),min(li))