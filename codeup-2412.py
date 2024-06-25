a = int(input())
age=0
for i in range(a):
    b = list(input().split(','))
    for i in b:
        try:
            i = int(i)
            age+=i       
        except:
            continue
print(f"{age/a:.2f}")