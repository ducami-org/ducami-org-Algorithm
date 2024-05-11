a=int(input())
b=str(2012-a+1)
if int(b[0]) == 1:
    print(f"{int(b)-1900} 1")
else:
    print(f"{int(b)-2000} 3")