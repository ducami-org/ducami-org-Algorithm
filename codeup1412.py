n = list(input().split())
n = list(str(n))

li = [0 for i in range(26)]

for i in range(len(n)):
    if 97 <= ord(n[i]) <= 122:  
        li[ord(n[i])-97] += 1
    else:
        continue
for i in range(len(li)):
    print(f"{chr(97+i)}:{li[i]}")
