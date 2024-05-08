cnt = 0
while True:
    cnt = 0
    a = input()
    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'A':
            cnt += 1
        elif a[i] == 'i' or a[i] == 'I':
            cnt += 1
        elif a[i] == 'o' or a[i] == 'O':
            cnt += 1
        elif a[i] == 'u' or a[i] == 'U':
            cnt += 1
        elif a[i] == 'e' or a[i] == 'E':
            cnt += 1
    if a == '#':
        break
    else:
        print(cnt)
    