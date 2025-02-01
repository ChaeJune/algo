import sys
import heapq

a, b= map(int, input().split())

def bfs_search(x, goal):

    oper = [lambda x: x+1, lambda x: x-1, lambda x: x*2]
    oper_nonzero = [lambda x: x+1, lambda x: x-1]
    oper_n = [lambda x: x-1]
    oper_zero = [lambda x: x*2]
    queue = [(0, x)]
    visited = set()
    cnt = 0
    while queue:
        depth, curr_x = heapq.heappop(queue)
        if curr_x == goal:
            return depth
        if curr_x in visited:
            continue

        #print(depth, curr_x)
        # -1 로 이유는 모르겠는데 이동해서 이렇게 되니까 -1에 2를 계속 곱해서 계속 아래로 내려감;
        # 0에서 -1로 가는 부분에서 x-1 연산이 실행되어서 그런듯
        visited.add(curr_x)



        if curr_x < goal:
            for op in oper_nonzero:
                new_x = op(curr_x)
                if new_x >= 0 and new_x<=100000:
                    heapq.heappush(queue,(depth + 1, new_x))

            for op in oper_zero:
                new_x = op(curr_x)
                if new_x >= 0 and new_x<=100000:
                    heapq.heappush(queue,(depth, new_x))

            
        else:
            for op in oper_n:
                new_x = op(curr_x)
                if new_x >= 0 and new_x<=100000:
                    heapq.heappush(queue,(depth + 1, new_x))
    return -1
    
ans = bfs_search(a, b)
print(ans)

#(32+1) * 2
