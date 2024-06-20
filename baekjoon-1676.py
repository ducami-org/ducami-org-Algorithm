a = int(input())
total=1; check=0
for i in range(1,a+1):
    total *= i

total = str(total)
new = list(total)
new.reverse()
for i in new:
    if(i!='0'):
        break
    check+=1
print(check)