# score = 0
# f_cnt = 0
# for i in range(20):
#     a,b,c = input().split()
#     b = float(b)
#     if c!='P':
#         if c=='A+':
#             score += (b* 4.5)
#         elif c=='A0':
#             score += (b* 4.0)
#         elif c=='B+':
#             score += b*3.5
#         elif c=='B0':
#             score += b* 3.0
#         elif c=='C+':
#             score += b*2.5
#         elif c=='C0':
#             score += b* 2.0
#         elif c=='D+':
#             score += b*1.5
#         elif c=='D0':
#             score += b*1.0
#         elif c == 'F':
#             f_cnt+=1
#     else:
#         continue
# if f_cnt == 20:
#     print(f"{score//20:.6f}")
# else:
#     print(f"{score/20:.6f}")


score = 0
total_credits = 0
for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        total_credits += b
        if c == 'A+':
            score += b * 4.5
        elif c == 'A0':
            score += b * 4.0
        elif c == 'B+':
            score += b * 3.5
        elif c == 'B0':
            score += b * 3.0
        elif c == 'C+':
            score += b * 2.5
        elif c == 'C0':
            score += b * 2.0
        elif c == 'D+':
            score += b * 1.5
        elif c == 'D0':
            score += b * 1.0
    else:
        continue

if total_credits == 0:
    print(f"0.000000")
else:
    print(f"{score / total_credits:.6f}")

