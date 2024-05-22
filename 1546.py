def positive_sign(a):
    if a > 0:
        print("plus")
    elif a < 0:
        print("minus")
    elif a == 0:
        print("zero")
num = int(input())
positive_sign(num)
