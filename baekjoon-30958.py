a = input()
b = list(input())
d=[0 for _ in range(97, 123)]
for i in b:
    if(i==' ' or i==',' or i=='.'):
        continue
    else:
        d[ord(i)-97]+=1
print(max(d))