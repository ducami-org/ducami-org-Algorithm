a = list(input().upper())
max_al = 0
c = 1
al = [0 for i in range(26)]
for i in range(len(a)):
    al[ord(a[i])-65] += 1
max_al = al.index(max(al))
b = chr(max_al + ord('A'))

if al.count(max(al)) > 1:
    print("?")
else:
    print(b)


# 대문자 A의 아스키코드값을 구해 그리고 가장
# 많이 나온 값의 인덱스를 구해 그리고 더해 
# 그다음에 다시 변환시켜서 알파벳으로 출력해
