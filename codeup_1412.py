a = input()
list = [0 for i in range(26)]
#a = 97
for i in range(len(a)):
    if ord(a[i])>=97 and ord(a[i])<=122:
        list[ord(a[i])-97]+= 1
for i in range(97, 123):
    print(f"{chr(i)}:{list[i-97]}")