a=input()
sum=0
sum1=0
for i in a:
    if i=='(':
        sum+=1
    elif i==')':
        sum1+=1
print(sum,sum1)