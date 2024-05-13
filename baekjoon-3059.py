a = int(input())
for i in range(a):
    b = input()
    total=2015
    d = [i for i in range(65, 91)]
    e=[0 for _ in range(65,91)]
    for j in b:
       if (ord(j) in d and e[ord(j)-65]==0):
           total -= ord(j)
           e[ord(j)-65]+=1
    print(total)
    