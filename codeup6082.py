#내 답안
a = int(input())
for i in range(1,a+1):
    if i%10==3 or i%10==6 or i%10==9:
        print('X',end=' ')
    else:
        print(i,end=' ')
#다른 답안
n = int(input())

for j in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')