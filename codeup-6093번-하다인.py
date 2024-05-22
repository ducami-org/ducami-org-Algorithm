a=int(input())
b=list(map(int, input().split()))

c= b[0]
for i in b:
   c= min(i, c)
print(c)