a,b,c = map(int,input().split())
d=['?']*a
for i in range(b):
    e = list(input())
    e = [e[i * c:(i + 1) * c] for i in range((len(e) + c - 1) // c )]
    for j in range(len(e)):
        if(e[j].count('?')!=len(e[j])):
            for k in e[j]:
                if(k!='?'):
                    d[j]=k
                    break

for i in d:
    print(i,end="")