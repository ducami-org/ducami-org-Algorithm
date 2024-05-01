a = input()
b = list()
for i in a:
    b.append(i)
b.sort(reverse=True)
for i in b:
    print(i,end="")