#내 답안
a,b,c = map(int,input().split())
d = int(input())
temp = a * 3600 + b * 60 + c + d
if temp // 3600 >24:
    print(f"{temp//3600-25} {temp%3600//60} {temp%60}")

elif  temp // 3600 == 24:
    temp -= a*3600
    print(f"{temp//3600-1} {temp%3600//60} {temp%60}")

else:
    print(f"{temp//3600} {temp%3600//60} {temp%60}")
    
#다른 답안
H, M, S = map(int, input().split())
D = int(input()) 

S += D % 60
D = D // 60
if S >= 60:
    S -= 60
    M += 1

M += D % 60
D = D // 60
if M >= 60:
    M -= 60
    H += 1

H += D % 24
if H >= 24:
    H -= 24

print(H,M,S)
