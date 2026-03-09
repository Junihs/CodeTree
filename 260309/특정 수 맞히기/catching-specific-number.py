# 무한반복
# 조건문으로 분기
# 25면 반복문 종료

while True:
    num = int(input())
    if num == 25:
        print("Good")
        break
    if num < 25:
        print("Higher")
    elif num > 25:
        print("Lower")
    