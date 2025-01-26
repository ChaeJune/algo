st = input()
l = len(st)
dp = [0]* l
tf_arr = [[False] * l for _ in range(l)]

for i in range(l):
    tf_arr[i][i] = True

for width in range(2, l + 1):
    for i in range(l - width + 1):
        j = i + width - 1
        if st[i] == st[j] and (width == 2 or tf_arr[j - 1][i+1]):
            tf_arr[j][i] = True


dp[0] = 1
 



for right in range(1,l):
    if not tf_arr[right][0]:
        dp[right] = right+1
    else:
        dp[right] = 1
    # dp[1][0] = min(dp[1][0], dp[0][0]+1)
    # dp[1][0] = min(dp[1][0], dp[1][1]+1)
    # when tf_arr[2][2] is true
    # dp[2][0] = min(dp[2][0], dp[1][0]+1)
    for left in range(1, right+1):
        if tf_arr[right][left]:
            dp[right] = min(dp[right], dp[left-1]+1)

print(str(dp[l-1]))
