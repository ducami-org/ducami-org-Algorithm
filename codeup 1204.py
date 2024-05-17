a = int(input())
if a%10 == 1 and a !=11:
    print(f"{a}st")
elif a%10 == 2 and a !=12:
    print(f"{a}nd")
elif a%10 == 3 and a != 13:
    print(f"{a}rd")
else:
    print(f'{a}th')