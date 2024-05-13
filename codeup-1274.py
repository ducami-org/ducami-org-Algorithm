a = int(input())
check=0
for i in range(1,a):
    if(a%i==0 and i!=1):
        check=1
        print('not prime')
        break
if(check==0):
    print('prime')