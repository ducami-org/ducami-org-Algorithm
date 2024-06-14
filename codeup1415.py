li = list(map(int,input().split()))
h = []
j = []
for i in range(10):
    if li[i] % 2 == 0:
        j.append(li[i])
    else:
        h.append(li[i])
if len(h) <= 0:
    print(max(j))
elif len(j) <= 0:
    print(max(h))
else:
    print(max(h),max(j))
