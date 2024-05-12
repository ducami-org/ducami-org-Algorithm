w=input()
sum1=0
sum2=0

for i in w:
    if i=='c' or i=='C':
        sum1+=1
    

for i in range(len(w)):
    if i==len(w)-1:
        pass
    else:
        if w[i]=='c'or w[i]=='C':
            if w[i+1]=='c' or w[i+1]=='C':
                sum2+=1
    
print(sum1)
print(sum2)



   

