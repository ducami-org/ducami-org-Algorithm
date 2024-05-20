a = list(input())
total=0
for i in a:
    total += int(i)
if(total%7==4):
    print('suspect')
else:
    print('citizen')