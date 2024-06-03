a = int(input())
money = a
ori_money = money
b = int(input())
n = list(map(int,input().split()))

for i in range(len(n)):
    if n[i] > 0:
        money = money + (n[i]/100) * money
    else:
        money = money + (n[i]/100) * money
result = money - ori_money

print(round(result))
if result < 0:
    print('bad')
elif result == 0:
    print('same')
else:
    print('good') 
