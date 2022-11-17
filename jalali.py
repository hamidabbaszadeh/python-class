def gregorian_to_jalali(gy, gm, gd):
    gy -= 1600
    gm -= 1
    gd -= 1
    g_day_no = 365 * gy + (gy + 3) // 4 - (gy + 99) // 100 + (gy + 399) // 400
    for i in range(0, gm):
        g_day_no += gregorian_month_days[i]
    if gm > 1 and ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0)):
        g_day_no += 1
    g_day_no += gd
    j_day_no = g_day_no - 79
    j_np = j_day_no // 12053
    j_day_no %= 12053
    jy = 979 + 33 * j_np + 4 * (j_day_no // 1461)
    j_day_no %= 1461
    if j_day_no >= 366:
        jy += (j_day_no - 1) // 365
        j_day_no = (j_day_no - 1) % 365
    for i in range(0, 11):
        if j_day_no >= jalali_month_days[i]:
            jm = i + 1
            jd = j_day_no - jalali_month_days[i]
    jm += 1
    jd += 1
    return (jy, jm, jd)

gregorian_month_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
jalali_month_days = [0, 31, 31, 31, 31, 31, 30, 30, 30, 30, 29, 29]

gy, gm, gd = 2023, 4, 7
jy, jm, jd = gregorian_to_jalali(gy, gm, gd)
print("Gregorian date: ", gy, "/", gm, "/", gd)
print("Jalali date: ", jy, "/", jm, "/", jd)
