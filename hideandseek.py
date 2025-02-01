import sys
from collections import deque

a, b= map(int, input().split())

def bfs_search(x, goal):

    oper = [lambda x: x+1, lambda x: x-1, lambda x: x*2]
    #oper_p = [lambda x: x+1, lambda x: x*2]
    oper_n = [lambda x: x-1]
    queue = deque([(x, 1)])
    visited = set()
    while queue:
        curr_x, depth = queue.popleft()
        if curr_x == goal:
            return depth
        if curr_x in visited:
            continue
        visited.add(curr_x)
        if curr_x < goal:
            for op in oper:
                new_x = op(curr_x)
                if x >= 0 and x<=100000:
                    queue.append((new_x ,depth + 1))
        else:
            for op in oper_n:
                new_x = op(curr_x)
                if x >= 0 and x<=100000:
                    queue.append((new_x ,depth + 1))
    return -1
    
ans = bfs_search(a, b)
print(ans-1)
