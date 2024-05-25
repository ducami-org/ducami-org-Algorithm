def f(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=1
    if sum==2:
        print('prime')
    else:
        print('composite')
n=int(input())
f(n)