d=[]
for i in range(5):
    d.append(int(input()))
d.sort()
print(sum(d)//len(d))
print(d[2])