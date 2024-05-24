a,b,c,d = map(int,input().split())
result = a
for i in range(1,d+1):
    if i == 1:
        result = a
    else:
        result = result *b+(c)
print(result)
