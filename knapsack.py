N, cap = map(int, input().split())

'''
def process(candidate, cap):
    second = []
    for i in range(len(candidate)):
        for j in range(i):
            #print(candidate[j])
            p, q = candidate[i]
            r, s = candidate[j]
            weight = p + r
            val = q + s
            if weight <= cap:
                second.append((weight, val))
    return second

'''


candidate = []

dp = [[0] * (cap+1) for _ in range(N+1)]

for i in range(N):
    w, v= map(int, input().split())
    candidate.append((w, v))

for weight in range(cap, -1, -1):
    cur_w, cur_v = candidate[0]
    if cur_w <= weight:
        dp[1][weight] = cur_v

#print(dp)
for i in range(2, N+1):
    for weight in range(cap, -1, -1):
        cur_w, cur_v = candidate[i-1]
        if cur_w > weight:
            dp[i][weight] = dp[i-1][weight]
        else:
            dp[i][weight] = max(dp[i-1][weight-cur_w] + cur_v , dp[i-1][weight])
#print(dp[N-1)[cap]) 하지 말것 index 한칸밀렸음
print(dp[N][cap])
