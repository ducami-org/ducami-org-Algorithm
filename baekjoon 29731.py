li = ["Never gonna give you up","Never gonna let you down","Never gonna run around and desert you","Never gonna make you cry","Never gonna say goodbye","Never gonna tell a lie and hurt you","Never gonna stop"]
a = int(input())
for i in range(a):
    b = input()
    if b not in li:
        print("Yes")
        break
    if a-1 == i:
            print("No")