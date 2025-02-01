import sys
from collections import deque

a, b= map(int, input().split())

def bfs_search(x, goal):

    oper = [lambda x: x+1, lambda x: x-1, lambda x: x*2]
    queue = deque([(x, 1)])
    while queue:
        curr_x, depth = queue.popleft()
        if curr_x == goal:
            return depth
        for op in oper:
            new_x = op(curr_x)
            if x >= 0 and x<=100000:
                queue.append((new_x ,depth + 1))
    return -1
    
ans = bfs_search(a, b)
print(ans-1)
