n = int(input())
cnt = 0
li_a = [0 for i in range(26)]
result = []

for i in range(n):
    a = list(input())
    li_a[ord(a[0])-97] += 1

for i in range(26):
    if li_a[i] > 4:
        cnt += 1
        result.append(chr(i+97))
if len(result) > 0: 
    for i in result:
            print(i,end='')
else:
    print('PREDAJA')

a,b = map(int,sys.stdin.readline().split())
a = list(str(a))
b = list(str(b))



