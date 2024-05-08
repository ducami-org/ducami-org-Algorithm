height, weight = map(float, input().split())
pyojun = (height - 100) * 0.9
biman = (weight - pyojun)  * 100 / pyojun
if biman