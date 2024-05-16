k = int(input())
for i in range(1, k+1):
    for j in range(k, 0, -1):
        if i<7 and j<7:
            if i+j == k:
                print(i, j)