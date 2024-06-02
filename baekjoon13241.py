# a,b = map(int,input().split())
# a_y = []
# b_y = []
# gy = []
# for i in range(1,a+1):
#     if a%i == 0:
#         a_y.append(i)
# for i in range(1,b+1):
#     if b%i == 0:
#         b_y.append(i)
# if len(a_y) > len(b_y):
#     for i in range(len(b_y)):
#         if b_y[i] in a_y:
#             gy.append(b_y[i])
# else:
#     for i in range(len(a_y)):
#         if a_y[i] in b_y:
#             gy.append(a_y[i])
# print(int((a*b)/max(gy)))

# a = int(input())
# b = int(input())
# c = int(input())
# sum = a+b+c

# if sum == 180:
#     if a==b==c:
#         print('Equilateral')
#     elif a==c and a==b:
#         print('Isosceles')
#     elif b==c and b == a:
#         print('Isosceles')

#     elif a!=c and a!=b:
#         print('Scalence')
#     elif b!=c and b != a:
#         print('Scalence')
  
# else:
#     print('Error')



a = int(input())
print(round(a))