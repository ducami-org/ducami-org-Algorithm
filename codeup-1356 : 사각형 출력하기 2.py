n=int(input())
c=0
for i in range(1,(n*2)):
    if i==n:
      print("*"*n)
      c=1
    elif(c==0):
      print("*"*i)
    elif(c==1):
       print("*"*(n-(i-n)))