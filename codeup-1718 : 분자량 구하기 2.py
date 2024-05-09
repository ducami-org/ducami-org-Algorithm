a=input()
if a=="CH":
    print("13")
else:
    b,c=a.split("H")

    if len(c)==0:
        print(int(b[1:])*12+1)
    elif len(b)==1:
        print(int(c)+12)
    else:
        print(int(b[1:])*12+int(c))
