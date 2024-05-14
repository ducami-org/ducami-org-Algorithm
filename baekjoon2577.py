b = []
sum_b = 0
arr = [0 for i in range(0,10)]
for i in range(3):
    b.append(int(input()))

sum_b = b[0]*b[1]*b[2]
for i in str(sum_b):
    arr[int(i)] += 1
for i in range(len(arr)):
    print(arr[i])