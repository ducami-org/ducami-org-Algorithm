l=[]
arr=[]
for i in range(10):
    n=int(input())
    l.append(n%42)
for i in l:
    if i not in arr:
        arr.append(i)
print(len(arr))
    