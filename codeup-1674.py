a = list(input())
count =0
for i in a:
    count += int(i)
if(count%7==4):
    print('Bad')
else:
    print('Good')