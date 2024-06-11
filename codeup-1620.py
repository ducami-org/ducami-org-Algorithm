a = list(input())
while True:
    total=0
    for i in a:
        total += int(i)
    if(total>=10):
        a = list(str(total))
        continue
    else:
        print(total)
        break

