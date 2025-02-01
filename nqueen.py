n = int(input())

mat = [[0]*n for _ in range(n)]

def dfs(num, downs, ups, verticals):
    if num == n:
        return 1
    acc = 0
    for j in range(n):
        if verticals[j] or downs[num-j+n-1] or ups[num+j]:
            #print("already")
            pass
        else:
            verticals[j] = downs[num-j+n-1] = ups[num+j] = True
            acc = acc + dfs(num+1, downs[:], ups[:], verticals[:])  
            verticals[j] = downs[num-j+n-1] = ups[num+j] = False  
            #print("acc:",acc)           
    return acc

verticals_q = [False]*n
downs_q = [False]*(2*n-1)
ups_q = [False]*(2*n-1)

temp = dfs(0, downs_q, ups_q, verticals_q)
print(temp)
