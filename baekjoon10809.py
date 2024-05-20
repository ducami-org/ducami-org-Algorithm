#첫번쨰 답안
# s = input()
# abc = 'abcdefghijklmnopqrstuvwsynz'

# for i in abc:
#     if i in s:
#         print(s.index(i),end=' ')
#     else:
#         print(-1,end=' ')
#두번쨰 답안
S = input()
check = [-1]*26
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')