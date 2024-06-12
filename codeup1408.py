n = input()
result = []
result2 = []
for i in range(len(n)):
    result.append(ord(n[i]) + 2)
for i in range(len(n)):
    result2.append((ord(n[i])*7)%80 + 48)
for i in range(len(n)):
    print(chr(result[i]),end='')
print()
for i in range(len(n)):
    print(chr(result2[i]),end='')