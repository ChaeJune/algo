N = int(input())  
arr = list(map(int, input().split()))  

dp = [1]*N

inv_dp = [1]*N
#print(dp)
for i in range(1, len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)



inv_arr = arr[::-1]
for i in range(len(inv_arr)):
    for j in range(i):
        if inv_arr[j] < inv_arr[i]:
            inv_dp[i] = max(inv_dp[i], inv_dp[j]+1)
    #print(inv_dp)
#print("---------")
#print(dp)
#print(inv_dp)

acc = -1
for i in range(N):
    acc = max(acc, dp[i]+inv_dp[N-i-1]-1)
print(acc)
