letter = input()

fruits = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for fruit in fruits:
    if letter in fruit[2] or letter in fruit[3]: 
        print(fruit)
        cnt += 1
    else:
        continue

print(cnt)