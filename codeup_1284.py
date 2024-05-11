n = int(input()) 
s = []
for i in range(2, n):
    if n % i == 0:
        s.append(i)
if len(s) == 2:
    if 4 in s: 
        print("wrong number")
    else:
        print(s[0], s[1])
else:
    print("wrong number")