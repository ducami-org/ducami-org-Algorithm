avg = 0
center = 0
b = []
for i in range(5):
    b.append(int(input()))
b.sort()
avg = sum(b)//len(b)
for i in range(5):
    if i ==2:
        center = b[i]
print(avg)
print(f'{int(center)}')

