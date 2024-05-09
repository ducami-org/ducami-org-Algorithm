a, b = map(int, input().split())

while True :
    
    if a >= 90 :
        break
    else :
        b += 1
        a += 5
print(b)