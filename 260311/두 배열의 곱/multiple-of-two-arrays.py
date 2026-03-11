arr1 = [list(map(int, input().split())) for _ in range(3)]
input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

result = [[0, 0, 0] for _ in range(3)]

for i in range(3):
    for j in range(3):
        result[i][j] = arr1[i][j] * arr2[i][j]
        print(result[i][j], end=" ")
    print()