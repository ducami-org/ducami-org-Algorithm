a = input()
d=[0 for _ in range(26)]
for i in a:
    if(ord(i)>=97 and ord(i)<=122):
        d[ord(i)-97]+=1
    
for i in range(len(d)):
    print(f"{chr(i+97)}:{d[i]}")