n, m = map(int, input().split())

# Please write your code here.
def rectangle(n, m):
    for _ in range(n):
        for _ in range(m):
            print(1, end="")
        print()


rectangle(n, m)