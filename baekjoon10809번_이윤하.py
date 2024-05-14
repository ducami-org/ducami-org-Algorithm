l=[-1 for i in range(26)]
A=[]
b=96
w=input()
for i in range(26):
    b+=1
    A.append(chr(b))

for i in range(len(A)):
    if A[i] in w:
        l[i]=w.index(A[i])
        
for i in l:
    print(i,end=' ')


