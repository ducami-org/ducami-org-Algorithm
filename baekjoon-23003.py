a = list(input())
for i in range(len(a)-1):
    if((a[i]=='d' or a[i]=='D') and a[i+1]=='2'):
        print('D2')
        exit()
print('unrated')