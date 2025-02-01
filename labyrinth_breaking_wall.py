import sys
from collections import deque

n, p = map(int, input().split())
map_data = []

for i in range(n):
    arr = list(input())
    map_data.append(arr)


def bfs_search(x, y, m, total):
    rows = n
    cols = p

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y, 1, True)])
    #m[y][x] = '0' 출발지점 0으로 되어잇음
    
    while queue:
        curr_x, curr_y, depth, flag = queue.popleft()
        #그러니까 False가 지나간 길이랑 True가 지나간 길은 사실 겹쳐도 됨.
        #False 일때는 2인 곳을 지나갈 수 있다 이말임
        #True 일때는 False가 지나간 곳으로 기록되는 곳을 지나갈 수 있어야함.
        #둘 다 지나간 경우에는? 걍 둘다 못지나가는 곳으로 다시 기록하면 됨
        if curr_x == cols - 1 and curr_y == rows - 1:
            total.append(depth)
            #return depth

        for dr, dc in directions:
            new_x, new_y = curr_x + dr, curr_y + dc

            if flag:
                if 0 <= new_x < cols and 0 <= new_y < rows and not m[new_y][new_x] == '2' and not m[new_y][new_x] =='6' and not m[new_y][new_x] == '1':
                    if m[new_y][new_x] == '0':
                        m[new_y][new_x] = '2'
                    elif m[new_y][new_x] == '3':
                        m[new_y][new_x] = '6'
                    queue.append((new_x, new_y, depth + 1, flag))
            else:
                if 0 <= new_x < cols and 0 <= new_y < rows and not m[new_y][new_x] == '3' and not m[new_y][new_x] =='6' and not m[new_y][new_x] == '1':
                    if m[new_y][new_x] == '2':
                        m[new_y][new_x] = '6'
                    elif m[new_y][new_x] == '0':
                        m[new_y][new_x] = '3'
                    queue.append((new_x, new_y, depth + 1, flag))

            
            if flag:
                if 0 <= new_x < cols and 0 <= new_y < rows and m[new_y][new_x] == '1':
                    #m[new_y][new_x] = '1'
                    queue.append((new_x, new_y, depth + 1, False))
    return total
    

total = []
ans = bfs_search(0, 0, map_data, total)
if total:
    print(min(total))
else:
    print(-1)
