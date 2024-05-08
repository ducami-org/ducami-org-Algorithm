a=input()
if a=="11" or a=="12" or a=="13":
    print(f"{a}th")
elif a[-1]=="1" :
    print(f"{a}st")
elif (a[-1]=="2"):
    print(f"{a}nd")
elif (a[-1]=="3"):
    print(f"{a}rd")
else:
    print(f"{a}th")