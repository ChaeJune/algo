#matrix

n = int(input())

acc = 0
storage = []
for i in range(n):

    a, b = map(int, input().split())
    if i == 0:
        storage.append(a)
        storage.append(b)
    else:
        storage.append(b)

    #storage.append((a, b))



dp = [[0] * (n + 1) for _ in range(n + 1)]

for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + storage[i - 1] * storage[k] * storage[j])

print(dp[1][n])
#print(storage)

    
