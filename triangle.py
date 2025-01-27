N = int(input())  
total_input = [] * N
for i in range(N):
    temp = list(map(int, input().split()))
    total_input.append(temp)
#print(arr)
#dp[][]
#0 (h = 0)
#01  (h = 1)
#012 -> 윗단계 0이면 01, 1이면 12
#0123 -> 윗단계 0이면 01, 1이면 12, 2면 23
dp = [[-float('inf')] * N for _ in range(N)]

#for arr in total_input:
    #dp[height][width]
    #dp[0][0] = max(dp[0][0], arr[0])
    #dp[0][1] = max(dp[0][1], dp[0][0]+arr[0])
    #dp[1][1] = max(dp[1][1], dp[0][0]+arr[1])

    # dp[1][2] = max(dp[1][2], dp[0][1]+arr[1])
    # dp[1][2] = max(dp[1][2], dp[1][1]+arr[1])

    # dp[][]
#print(total_input)
dp[0][0] = total_input[0][0]

for h in range(1,N):
    cur = total_input[h]
    for i in range(h+1):
        dp[i][h] = max(dp[i][h], dp[i][h-1]+ cur[i])
        dp[i][h] = max(dp[i][h], dp[i-1][h-1]+ cur[i])


final = []
for i in range(N):
    final.append(dp[i][N-1])
print(max(final))


