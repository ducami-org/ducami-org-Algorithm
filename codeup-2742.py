a = int(input())
d=[0]*7
day=['월','화','수','목','금','토','일']
count=0
for i in range(a):
    b = list(input())
    for j in range(7):
        if(b[j]=='1'):
            d[j]+=1
            
for i in range(7):
    if(d[i]==a):
        print(f'{day[i]}요일에 가능')
        count+=1
if(count==0):
    print('다음에 만나요~')