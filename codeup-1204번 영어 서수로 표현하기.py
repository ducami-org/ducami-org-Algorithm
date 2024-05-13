a = input()
a = int(a)
b = ''

if(a % 10 == 1):
    b = str(a) + 'st'
    if(a == 11):
        b = str(a) + 'th'
elif(a % 10 == 2):
    b = str(a) + 'nd'
    if(a == 12):
        b = str(a) + 'th'
elif(a % 10 == 3):
    b = str(a) + 'rd'
    if(a == 13):
        b = str(a) + 'th'
else:
    b = str(a) + 'th'
print(b)