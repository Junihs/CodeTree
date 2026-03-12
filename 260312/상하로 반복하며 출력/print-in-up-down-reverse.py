N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]


for j in range(N):
    num = 1
    for i in range(N):
        if j % 2 == 0:
            arr[i][j] = num
            num += 1
        else:
            arr[N-(i+1)][j] = num
            num += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end="")
    print()

       

        