d=[]
for i in range(9):
   d.append(int(input())) 
print(max(d),d.index(max(d))+1,sep="\n")