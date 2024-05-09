a, b = input().split()
op = ['+', '-', '*', '/']
for i in range(4):
    print(a + op[i] + b + '=' , int(eval(a + op[i] + b)), sep = '')
