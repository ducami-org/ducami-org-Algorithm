arr=input()
num1=0
num2=0
if "+" in arr:
    num1,num2=map(int,arr.split("+"))
    print(num1+num2)
elif  "-" in arr:
    num1,num2=map(int,arr.split("-"))
    print(num1-num2)
elif  "*" in arr:
    num1,num2=map(int,arr.split("*"))
    print(num1*num2)
elif  "/" in arr:
    num1,num2=map(int,arr.split("/"))
    print(int())