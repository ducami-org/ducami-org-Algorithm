a = int(input())
sum = 0
for i in range(a, 0, -1):
    print(" "*sum,end='')
    print("*"*i)
    sum+=1