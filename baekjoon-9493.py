hour_to_sec = 3600
min_to_sec = 60
while True:
    m, a, b = map(float, input().split())
    if m == a == b == 0:
        break
    t = round((m / a - m / b) * hour_to_sec)
    h = t // hour_to_sec
    m = (t % hour_to_sec) // min_to_sec
    s = t % min_to_sec
    print("%d:%02d:%02d" % (h, m, s))
    
    """
    21 70 80
    A : 0.3h
    B : 0.2625h
    A-B = 0.0375h*60 = ~ m
    0.4
    0.325
    0.065
"""