a = []
final = []
c = 0
for i in range(1, 11):
    b = int(input())
    a.append(b%42)
for i in range(10):
    if a[i] not in final:
        c+=1
        final.append(a[i])
print(c)