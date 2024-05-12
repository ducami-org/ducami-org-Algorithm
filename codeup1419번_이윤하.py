w=input()
sum=0
for i in range(len(w)):
    if w[i]=='l' and w[i+1]=='o' and w[i+2]=='v' and w[i+3]=='e':
        sum+=1
print(sum)