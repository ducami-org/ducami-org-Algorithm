plusData, Data = [], []
a, b = map(int, input().split())
for i in range(a):
    c = list(map(int, input().split()))
    Data.append(c)
for i in range(a):
    c = list(map(int, input().split()))
    plusData.append(c) 
for i in range(a):
    for j in range(b):
        print(plusData[i][j] + Data[i][j], end=' ') 
    if b-1 != i: 
        print() 