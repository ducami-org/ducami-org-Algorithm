a,b = map(int,input().split())
if a%2==0 and b%2==0:
    if (a+b)%2==0:
        print('짝수+짝수=짝수')
    else:
        print('짝수+짝수=홀수')
elif a%2==1 and b%2==1:
    if (a+b) %2==0:
        print('홀수+홀수=짝수')
    else:
        print('홀수+홀수=홀수')
elif a%2==0 and b%2==1:
    if (a+b)%2==0:
        print('짝수+홀수=짝수')
    else:
         print('짝수+홀수=홀수')
elif a%2==1 and b%2==0:
    if (a+b)%2==0:
        print('홀수+짝수=짝수')
    else:
         print('홀수+짝수=홀수')
