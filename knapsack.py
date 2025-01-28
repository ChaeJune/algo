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

dp = [[0] * (cap+1) for _ in range(N)]

for i in range(N):
    w, v= map(int, input().split())
    candidate.append((w, v))

for i in range(1,N):
    for weight in range(cap, -1, -1):
        cur_w, cur_v = candidate[i]
        if cur_w > weight and dp[i][weight] != -1:
            dp[i][weight] = dp[i-1][weight]
        elif dp[i][weight] != -1 :
            dp[i][weight] = max(dp[i-1][weight-cur_w] + cur_v , dp[i-1][weight])
        else:
            pass
print(dp[N-1][cap])

#tp = candidate
#for i in range(N-1):
#    tp = process(tp,cap)
#    print(tp)
#    print("-----------------------")
#bag
#0 1 2 3 4
#012, 123, 234


# 물건 개수가 1일때 최대인 값 찾기 => 물건 개수가 2일때 최대인 값 찾기, 물건 개수가 3일때 최대인 값 찾기, 물건 개수가 4일때 최대인 값 찾기 ... 
# 물건 2개인 상황 물건 개수가 1개일때 물건을 제외하고 2개일 때 최대인 값을 찾아야 함. 물건 3개일때도 똑같이.
# 근데 이거 어떤 물건을 골랐는지를 체크해야 한다는 사실이 뭔가 거북함. 왜 거북한지 생각해보면 이 log를 싹다 남겨야 해서 그런 것 같음
# 뭔가 그냥 하나 넣을때마다 이거를 고른 경우 안고른 경우를 체크해야 하는건가 싶기도 하고
# dp[] = max(dp[], selected + ) if selected + dp[] <= cap 
# 가능한 모든 조합을 시도해본다? XOXXO 이런식으로 배열을 정리해서 => N개 있다고 하면 N!을 다 검사해야함 좀 아닌듯
# dp 배열을 만들어서 capacity 안에 담을 수 있으면 capacity - weight 해서 새로운 주머니의 capacity w를 만듦.
# i 번째 원소가 새로운 capacity c에 대해서 c-w_i < 0 인 경우에는 그냥 그 다음으로 넘어갈 수밖에 없음
# i 번째 원소가 새로운 capacity c에 대해서 c-w_i > 0 인 경우에는 v_i 가 i번째 물건의 가치라고 했을 때, max(dp[i-1][cap], v_i + dp[i-1][cap-w_i]) 로 dp[i][cap] 을 갱신
# i = 0 이거나 cap 이 0인 경우 => 그냥 0임..
# dp 배열
# cap을 넘었는지를 언제 체크하는지가 관건일 것 같다.
