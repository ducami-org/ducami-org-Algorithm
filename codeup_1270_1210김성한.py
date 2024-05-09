n = input()
sum = 0
for i in range(1, int(n)+1):
    if (str(i)[-1]) == "1":
        sum +=1
print(sum)