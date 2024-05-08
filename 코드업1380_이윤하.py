k=int(input())
for i in range(1,k):
    for j in range(1,k):
        if i+j==k:
            if i>6 or j>6:
                pass
            else:
                print(i,j)
            