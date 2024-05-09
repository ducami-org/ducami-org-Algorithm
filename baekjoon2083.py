while True:
    a,b,c = input().split()
    b = int(b)
    c = int(c)
    if b > 17 or c >= 80:
        print(f"{a} Senior")
    elif a == '#' and b==0 and c == 0:
        break
    else:
        print(f"{a} Junior")