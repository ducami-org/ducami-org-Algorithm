def sum(a, b):
    n = 0
    for i in range(a):
        if "tap" in b[i]:
            print(b[i])
            n+=1
        elif len(b[i])<=3:
            print(b[i])
            n+=1
        elif "xocure" in b[i]:
            print(b[i])
            n+=1
    if n >3 and n < 7:
        print("warning")
    elif n>=7:
        print("danger")
    else:
        print("safe")
a = int(input())
b= []
for i in range(a):
    c = input()
    b.append(c)
sum(a, b)