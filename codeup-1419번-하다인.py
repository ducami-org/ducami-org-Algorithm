a = input()
b = 0
for i in range(len(a)):
    if a[i:i+4] == "love":
        b += 1
print(b)