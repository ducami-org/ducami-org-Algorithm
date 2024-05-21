a, b = int(input().split())
a+= 24
b = b + a * 60
b -= 30
a = b/ 60
a= a% 24
b= b % 60
print(a ,b)