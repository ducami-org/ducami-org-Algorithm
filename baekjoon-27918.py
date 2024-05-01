a= int(input())
D=0
P=0
for i in range(a):
   b= input()
   if(b=='D'):
       D+=1
   elif(b=='P'):
       P+=1
   if(D-P>=2 or P-D>=2):
        break

print(f"{D}:{P}") 