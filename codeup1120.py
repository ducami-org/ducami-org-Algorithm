a = list(map(int,input().split()))
b = 0
for i in range(len(a)):
    b += a[i]
print("{0:.2f}".format(b/len(a)))