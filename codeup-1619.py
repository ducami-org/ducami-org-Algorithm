a = input()
s = 0
for i in a:
    s += int(i)
if(int(a)%s == 0):
    print('Yes')
else:
    print('No')