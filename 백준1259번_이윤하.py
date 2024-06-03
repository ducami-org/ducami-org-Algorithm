
while True:
    w=input()
    if w=='0':
        break
    l=[]
    for i in range(len(w)-1,-1,-1):
        l.append(w[i])
    
    if w==(''.join(l)):
        print('yes')
    else:
        print('no')

