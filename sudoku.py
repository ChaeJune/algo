def dfs(table, verticals, horizontals, squares):
    for row in range(9):
        for col in range(9):
            if table[row][col] == 0:
                for num in range(1, 10):
                    if not (verticals[col][num-1] or horizontals[row][num-1] or squares[(row//3)*3 + (col//3)][num-1]):
                        horizontals[row][num-1] = verticals[col][num-1] = squares[(row//3)*3 + (col//3)][num-1] = True
                        table[row][col] = num
                        if dfs(table, verticals, horizontals, squares):
                            return True
                        table[row][col] = 0
                        horizontals[row][num-1] = verticals[col][num-1] = squares[(row//3)*3 + (col//3)][num-1] = False
                return False
    return True
            


n = 9
verticals = [[False]*n for _ in range(n)]
horizontals = [[False]*n for _ in range(n)]
squares = [[False]*n for _ in range(n)]
table = []
#print(verticals)

for i in range(9):
    arr = list(map(int, input().split()))  
    table.append(arr)
    for j in range(9):
        if arr[j] != 0:
            #행으로 봤을 때 어떤 원소가 부족한지를 알아내야 함.
            #열로 봤을 때도 알아내야 하니까 horizontal이 필요한거임.
            #table[i][j] = arr[j]
            verticals[j][arr[j]-1] = True
            horizontals[i][arr[j]-1] = True
            t = (i//3)*3 + (j//3)
            squares[t][arr[j]-1] = True


#temp = dfs(table, verticals, horizontals, squares)


if dfs(table, verticals, horizontals, squares):
    for row in table:
        for item in row:
            print(item, end=' ')
        print("")
