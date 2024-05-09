a, b = map(int, input().split())
if a % 2 !=0:
    print("홀수",end='+')
    if b % 2 !=0:
        print("홀수",end='=')
        print("짝수")
    else:
        print("짝수",end='=')
        print("홀수")
else:
    print("짝수",end='+')
    
    if b % 2 !=0:
        print("홀수",end='=')
        print("홀수")
    else:
        print("짝수",end='=')
        print("짝수")