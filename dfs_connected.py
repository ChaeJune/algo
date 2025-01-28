import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())

map = []

for i in range(n):
    arr = list(input())  
    map.append(arr)


def search(x, y, m):
    if x < 0 or x >= n or y < 0 or y >= n or m[y][x] == '0':
        return 0


    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    if m[y][x] == '1':
        count = 1
        m[y][x]='0'
    else:
        print('hi')
        return 0
    for dr, dc in directions:
        count += search(x + dr, y + dc, m)
    return count


ans = []
for i in range(n):
    for j in range(n):
        if map[i][j] != '0':
            num = search(j, i, map)
            ans.append(num)
final = sorted(ans)
print(len(final))
for item in final:
    print(item)
