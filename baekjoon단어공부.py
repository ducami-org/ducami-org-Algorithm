#내 답안
a = list(input().upper())
b = [0]*26
for i in a:
    b[ord(i)-65]+=1
    

    








#다른답안
# a = list(input().upper())
# a_set = list(set(a))
# a_count = [ a.count(i)for i in a_set]

# if a_count.count(max(a_count)) != 1:
#     print('?')
# else:
#     idx = a_count.index(max(a_count))
#     print(a_set[idx])