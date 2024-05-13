food = {'1':'400', '2':'340', '3':'170', '4':'100', '5':'70'}
a, b = input().split()

if int(food[a]) + int(food[b]) > 500:
    print('angry') 
else:
     print('no angry')