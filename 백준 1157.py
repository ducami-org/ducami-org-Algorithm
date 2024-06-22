a = input()
a = a.upper()
n = 0
temp = a.count("A")
tempa = "A"
for i in range(66, 91):
    if len(a) > 1:
        if a.count(chr(i)) > temp:
            temp = a.count(chr(i))
            tempa = chr(i)
            n = 0
        elif a.count(chr(i)) == temp:
            if a.count(chr(i)) != 0:
                n+=1
    else:
        tempa = a
if n>0:
    print('?')
else:
    print(tempa)