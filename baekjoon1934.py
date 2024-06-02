# n = int(input())
# d = True
# for i in range(n):
#     c = 1
#     a,b = map(int,input().split())
#     a_a = a
#     b_b = b
#     if a>b:
#         while c != 0:
#             if a%b == 0:
#                 c = b
#                 d = False
#             c = a%b
#             a = b
#             b = c
        
#     else:
#         while c != 0:
#             if b%a == 0:
#                 c = a
#                 d = False
#             c = b%a
#             b = a
#             a = c
        
#     if c == 0:
#         c += 1
#     print(int((a_a*b_b)/c))

n = int(input())
im = True
for i in range(n):
    a,b = map(int,input().split())
    if a > b:
        while im == True:
            if b%c == 0:
                im = False
                c = a%b
                a = b
                b = c
    else:
        while im == True:
            if a%c == 0:
                im = False
                c = b%a
                b = a
                b = c
    
                


            