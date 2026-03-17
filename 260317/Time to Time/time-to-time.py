a, b, c, d = map(int, input().split())

# Please write your code here.
hour, minute = a, b
time = 0

while True:
    if hour == c and minute == d:
        break
    
    time += 1
    minute += 1

    if minute == 60:
        hour += 1
        minute = 0

print(time)