n=int(input())
sum=n
for i  in range(n):
    w=input()
    for i in range(len(w)-1):
        if w[i]==w[i+1] :
            pass
        elif w[i] in w[i+1:]:
            sum-=1
print(sum)