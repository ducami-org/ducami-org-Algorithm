d=[0 for _ in range(97,123)]
while True:
    try:
        a = list(input())
        for i in a:
            if(i==' '):
                continue
            else:
                d[ord(i)-97]+=1
    except:
        break

for i in range(26):
    if(max(d)==d[i]):
        print(chr(i+97),end="")