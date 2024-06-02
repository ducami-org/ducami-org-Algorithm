a = int(input())
b = a
cur = 0
im = True
new = 0
cnt = 0
while im:
    cnt += 1
    cur = a//10 + a%10
    new = (a%10)*10 + cur%10
    if new == b:
        print(cnt)
        im = False 
    else:   
        a = new

    