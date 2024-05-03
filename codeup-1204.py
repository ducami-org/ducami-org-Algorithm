a  =int(input())
if(a>=11 and a<=20):
    print(f"{a}th")
else:
    if(a%10==1):
        print(f"{a}st")
    elif(a%10==2):
        print(f"{a}nd")
    elif(a%10==3):
        print(f"{a}rd")
    else:
        print(f"{a}th")   