def sum(num, temp=0):
    for i in range(len(num)):
        temp += int(num[i])
    if len(str(temp)) == 1:
        print(temp)
        return 0
    else:
        sum(str(temp))
num = input()
sum(num)