num = int(input())
a = 'prime'

for i in range(2, num):
    if num % i == 0:
        a = 'not prime'
        break

print(a)