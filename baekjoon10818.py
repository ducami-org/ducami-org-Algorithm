#내 답안
a = int(input())
b = list(map(int,input().split()))
b.sort()
print(b[0],b[-1])
#다른 답안1
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))
#다른답안 2
cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)