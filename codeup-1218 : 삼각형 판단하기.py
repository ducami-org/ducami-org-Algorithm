a,b,c=map(int,input().split())
if a+b>c and c+a>b and c+b>a:
    if a==b and b==c :
        print("정삼각형")
    elif a==b or b==c or c==a :
        print("이등변삼각형")
    elif (a*a)+(b*b)==c*c:
        print("직각삼각형")
    else :
        print("삼각형")
else:
    print("삼각형아님")