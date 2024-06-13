n = int(input())
li = [0 for i in range(n)]
for i in range(n-1):
   a = int(input())
   li[a-1] = a

for i in range(n):
   if li[i] == 0:
      print(li.index(li[i])+1)