a = int(input()) # 투자한 액수
b = int(input()) # 투자 일 수
data = list(map(int, input().split()))
result = a

for i in data:
    result = result + (result * (i * 0.01))

print(round(result - a))
if (result - a == 0):
    print('same')
elif(result - a < 0):
    print('bad')
else:
    print('good')