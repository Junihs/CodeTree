N = int(input())
row = []

for i in range(N):
    row = []

    for j in range(1, N+1):
        row.append(j)
    
    if i % 2 == 0:
        for j in range(N):
            print(row[j], end="")
    else:
        for j in range(N-1, -1, -1):
            print(row[j], end="")
    
    print()





