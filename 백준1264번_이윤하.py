l=['e','a','o','i','u','E','A','I','O','U']
s=1

while True:
    s=input()
    
    if s=='#':
        break

    sum=0
    for i in s:
        if i in l:
            sum+=1

    print(sum)
    
    