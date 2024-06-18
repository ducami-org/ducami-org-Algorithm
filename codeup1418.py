n = input()
cnt = 0
result = []
for i in range(len(n)):
    cnt += 1
    if n[i] == 't':
        result.append(cnt)
    else:
        continue
for i in result:
    print(i,end =' ')