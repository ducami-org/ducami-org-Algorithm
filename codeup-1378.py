a = int(input())
d = [i for i in range(1,a+1)]
total =0
for i in range(a):
    total += d[i]*(a-i)
        
print(total)