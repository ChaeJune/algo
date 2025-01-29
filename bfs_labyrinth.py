import sys
from collections import deque

n, p = map(int, input().split())
map_data = []

for i in range(n):
    arr = list(input())
    map_data.append(arr)


def bfs_search(x, y, m):
    rows = n
    cols = p

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y, 1)])
    m[y][x] = '0'
    while queue:
        curr_x, curr_y, depth = queue.popleft()

        if curr_x == cols - 1 and curr_y == rows - 1:
            return depth

        for dr, dc in directions:
            new_x, new_y = curr_x + dr, curr_y + dc

            if 0 <= new_x < cols and 0 <= new_y < rows and m[new_y][new_x] == '1':
                m[new_y][new_x] = '0'
                queue.append((new_x, new_y, depth + 1))

    return -1


ans = bfs_search(0, 0, map_data)
print(ans)
