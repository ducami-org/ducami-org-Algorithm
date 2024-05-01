d=list()
a = int(input())
b = input()
total =0

for i in b:
    d.append(ord(i)-96)
    
for i in range(len(d)):
    total += d[i]*(31**i)
    
print(total%1234567891)