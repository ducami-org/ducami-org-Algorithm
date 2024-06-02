n,m=input().split() #123
sum = 0
rv=""
for i in n:
    rv=i+rv
rv2=''
for i in m:
    rv2 = i+rv2
sum = int(rv) + int(rv2)
rv3 = ''
for i in str(sum):
    rv3 = i+rv3
print(int(rv3))