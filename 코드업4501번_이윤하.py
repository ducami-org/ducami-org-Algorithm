l=[]
for i in range(7):
    l.append(int(input()))

a=l.pop(l.index(max(l)))
print(a)
print(max(l))