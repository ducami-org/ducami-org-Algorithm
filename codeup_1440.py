a = int(input())
b = list(map(int, input().split()))
for i in range(a):
    print(f"{i+1}: ", end='')
    for j in range(len(b)):
        if i != j:
            if b[i] > b[j]:
                print(">", end=' ')
            elif b[i]<b[j]:
                print("<", end=' ')
            else:
                print("=", end=' ')
    print()