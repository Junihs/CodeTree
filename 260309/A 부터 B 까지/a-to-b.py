A, B = map(int, input().split())

while B >= A:
    if A % 2 == 1:
        print(A, end=' ')
        A *= 2
    else:
        print(A, end=' ')
        A += 3
