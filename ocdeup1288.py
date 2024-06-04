a,b = map(int,input().split())
n1 = 0
n2 = 0
sum = 0
n3 = 0
if a > b:
    n1 = a-b
    n2 = b
    n3 = a
    for i in range(n1-1,0,-1):
      n1 *= i
    for i in range(b-1,0,-1):
      n2 *= i
    for i in range(a-1,0,-1):
      n3 *= i   
else:
    n1 = b-a
    n2 = a
    n3 = b
    for i in range(n1-1,0,-1):
      n1 *= i
    for i in range(b-1,0,-1):
      n2 *= i  
    for i in range(b-1,0,-1):
       n3 *= i
       
sum = n2 * n1
if a == b:
   print(1)
else:
    print(int(n3/sum))