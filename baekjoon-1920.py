a =int(input())
for i in range(a):
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    if(b[0]+b[1]*2+b[2]*3+b[3]*3+b[4]*4+b[5]*10 == c[0]+c[1]*2+c[2]*2+c[3]*2+c[4]*3+c[5]*5+c[6]*10):
        print(f'Battle {i+1}: No victor on this battle field')
    elif(b[0]+b[1]*2+b[2]*3+b[3]*3+b[4]*4+b[5]*10 > c[0]+c[1]*2+c[2]*2+c[3]*2+c[4]*3+c[5]*5+c[6]*10):
        print(f'Battle {i+1}: Good triumphs over Evil')
    else:
        print(f'Battle {i+1}: Evil eradicates all trace of Good')
        
