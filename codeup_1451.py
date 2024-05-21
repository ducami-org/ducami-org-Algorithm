a = int(input())
list = []
for i in range(a):
    c = int(input())
    list.append(c)
list = sorted(list)
for i in range(a):
    print(list[i])