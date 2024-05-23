a = list(input().upper())
max_al = 0
c = 1
al = [0 for i in range(26)]
for i in range(len(a)):
    al[ord(a[i])-65] += 1
max_al = al.index(max(al))
b = chr(max_al + ord('A'))

if al.count(max(al)) > 1:
    print("?")
else:
    print(b)




