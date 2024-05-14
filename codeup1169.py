a = int(input())
year = 2012
year_a = year-a+1
if year_a//100 == 20:
    print(year_a%100,3)
elif year_a//100 == 19:
    print(year_a%100,1)
else:
    print(0,1)