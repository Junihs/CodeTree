m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month, day = m1, d1
days = 1

m_31 = [1, 3, 5, 7, 8, 10, 12]
m_30 = [4, 6, 9, 11]
while True:
    if month == m2 and day == d2:
        break
    
    day += 1
    days += 1

    if month in m_31:
        if day == 32:
            month += 1
            day = 1
    
    elif month in m_30:
        if day == 31:
            month += 1
            day = 1
    
    elif month == 2:
        if day == 29:
            month += 1
            day = 1

print(days)