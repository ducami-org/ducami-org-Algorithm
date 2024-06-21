a = int(input())
b = int(input())
sum = a*31 + b
if sum > 80:
    print('After')
elif sum == 80:
    print('Special')
else:
    print('Before')