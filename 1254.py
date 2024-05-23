al = list(map(ord, input().split()))
al.sort()
for i in range(al[0], al[1] + 1):
    print(chr(i),end=' ')