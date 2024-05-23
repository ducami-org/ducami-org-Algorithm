num = list(map(int, input().split())) 
num.sort() 
for i in range(num[0], num[1] + 1): 
    print(i, end=' ')
