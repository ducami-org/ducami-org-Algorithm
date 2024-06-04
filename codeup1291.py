n = input()
n = list(str(n))
sum = 0
for i in range(len(n)):
    sum += int(n[i])
if sum % 7 == 4:
    print('suspect')
else:
    print('citizen') 