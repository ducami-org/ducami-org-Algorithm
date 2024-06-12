def a(sum):
    c = ""
    d = ""
    s = list(sum)
    s.reverse()
    for i in range(len(s)):
        c += s[i]
    b = str(int(c) + int(sum))
    br = list(b)
    br.reverse() 
    for j in range(len(br)):  
        d += br[j]
    if b == d:
        return "YES"
    else:
        return "NO"

sum = input()
print(a(sum))
