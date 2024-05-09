arr=[]
for i in range(10):
    arr.append(input().split())
x, y = 1, 1
while x <= 8 and y <= 8:
    if arr[x][y] == "2":
        arr[x][y] = "9"
        break
    arr[x][y] = "9"
    if  arr[x][y+1] == "1" and   arr[x+1][y] == "1":
        break
    elif    arr[x][y+1] == "1":
        x += 1
    else:
        y += 1
for i in range(10):
    for j in range(10):
        print(arr[i][j],end=' ')
    print()