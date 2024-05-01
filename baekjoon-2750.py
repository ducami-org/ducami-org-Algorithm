a =int(input())
d = []
for i in range(a):
    b = int(input())
    d.append(b)
    
d.sort(reverse=False)
for i in d:
    print(i)