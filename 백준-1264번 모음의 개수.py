a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    cnt = 0
    s = input()
    if s == '#':
        break
    for s in s:
        if s in a:
            cnt += 1
    print(cnt)