af = ""
bf = ""
a, b = input().split()
for i in range(len(a)-1, -1, -1):
    af += a[i]
for i in range(len(b)-1, -1, -1):
    bf += b[i]
if int(af) >= int(bf):
    print(int(af))
elif int(bf) >= int(af):
    print(int(bf))