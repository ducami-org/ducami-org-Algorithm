a = int(input())
for i in range(a):
    x,y = input().split()
    if(y=='kg'):
        print(f"{float(x)*2.2046:.4f} lb")
    elif(y=='lb'):
        print(f"{float(x)*0.4536:.4f} kg")
    elif(y=='l'):
        print(f"{float(x)*0.2642:.4f} g")
    else:
        print(f"{float(x)*3.7854:.4f} l")