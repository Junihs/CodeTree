n, m = map(int, input().split())

# Please write your code here.
def great_com_div(n, m):
    result = 0
    if n < m:
        for i in range(1, n):
            if n % i == 0 and m % i == 0:
                result = i
        print(result)
        
    elif n > m:
        for i in range(1, m):
            if n % i == 0 and m % i == 0:
                result = i
        print(result)

great_com_div(n, m)