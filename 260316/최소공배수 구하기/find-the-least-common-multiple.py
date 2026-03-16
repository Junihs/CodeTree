n, m = map(int, input().split())

# Please write your code here.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    result = 0
    result = a * b // gcd(a, b)
    print(result)

lcm(n, m)