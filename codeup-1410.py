a = input()
b=0; c=0
for i in a:
    if(i=='('):
        b +=1
    else:
        c += 1
        
print(b,c)