# n = input()
# for i in range(len(n)):
#     if 97 <= ord(n[i]) <= 122:
#         print(n[i].upper(),end='')
#     else:
#         print(n[i].lower(),end='')


n = int(input())
result = []
max_y = []
max_m = []
max_d = []
name = []
for i in range(n):
    n,d,m,y = input().split()
    max_y.append(int(y))
    max_m.append(int(m))
    max_d.append(int(d))
    name.append(n)
if max_y.count(max(max_y)) != 0:
    
            
