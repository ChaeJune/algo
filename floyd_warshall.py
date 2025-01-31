n = int(input())
m = int(input())
mat = [[float('inf')]*(n+1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    #서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
    #mat[a][b] = min(mat[a][b], c)
    #mat[b][a] = min(mat[b][a], c)
    mat[a][b] = min(c, mat[a][b])
    #mat[b][a] = c
#print(mat)

for i in range(n+1):
    mat[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1): 
            mat[i][j] = min(mat[i][j],mat[i][k]+mat[k][j])

#print(mat)

for i in range(1,n+1):
    for j in range(1, n+1):
        if mat[i][j] != float('inf'):
            print(mat[i][j], end =' ')
        else:
            print(0, end = ' ')
    print("")
