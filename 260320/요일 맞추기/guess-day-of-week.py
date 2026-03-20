m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# 30일인 달 -> 달 변경시 30일 추가
# 31일인 달 -> 달 변경시 31일 추가
# m1, m2 바교에서 큰 수의 -1까지
m_30 = [4, 6, 9, 11]
m_31 = [1, 3, 5, 7, 8, 10, 12]

sign 

days = 0
while True:
    if m1 == m2:
        days += d2 - d1
        break
    
    if m1 in m_30:
        days += 30
    elif m1 in m_31:
        days += 31
    elif m1 == 2:
        days += 28
    m1 += 1

def dow(d):
    if d % 7 == 0:
        print("Mon")
    elif d % 7 == 1:
        print("Tue")
    elif d % 7 == 2:
        print("Wed")
    elif d % 7 == 3:
        print("Thu")
    elif d % 7 == 4:
        print("Fri")
    elif d % 7 == 5:
        print("Sat")
    else:
        print("Sun")

dow(days)