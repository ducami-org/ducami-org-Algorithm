a = int(input())
b = int(input())
c = list(map(int, input().split()))
sum = a
for i in range(b):
    sum = sum+sum*(c[i]/100)
sum = round(sum-a)
print(sum)
if sum<0:
    print("bad")
elif sum == 0:
    print("same")
else:
    print("good")