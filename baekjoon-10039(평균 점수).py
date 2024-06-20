arr=[]
for i in range(5):
    n=int(input())
    if n<40:
        arr.append(40)
    else:
        arr.append(n)
s=sum(arr)
print(s//5)