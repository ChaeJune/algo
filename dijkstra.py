import heapq

v, e = map(int, input().split())

start = int(input())
mat = [[float('inf')]*(v+1) for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    #서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
    #mat[a][b] = min(mat[a][b], c)
    mat[b][a] = min(mat[b][a], c)


#print(mat)

'''
print('')
for i in range(1,v+1):
    for j in range(1,v+1):
        print(mat[i][j], end =' ')
    print('')
'''

#priority queue



d = [float('inf')]*(v+1) #distance
#print(d)
d[start] = 0
pq = [(0, start)]
visited = set()

while pq:
    dist, cur = heapq.heappop(pq)
    if cur in visited:
        continue
    visited.add(cur)
    #pq.heappush()
    for i in range(1,v+1):
        if mat[i][cur] != float('inf'):
            dist = d[cur] + mat[i][cur]
            d[i] = min(d[i], dist) # same as d[i]
            if dist == d[i]:
                heapq.heappush(pq, (dist, i))

for tp in range(1, v+1):
    if d[tp] == float('inf'):
        print("INF")
    else:
        print(d[tp])






#heapq.heappush()
