n=int(input())
count=0
list=[]

for i in range(2, n):
    if n % i == 0:
        list.append(i)

if len(list) >= 2:
    if 4 in list:  
        print("wrong number")
    else:                              
        for i in list:
            print(i,end=" ")

else:
    print("wrong number")
        