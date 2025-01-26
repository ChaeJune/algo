import sys
#sys.setrecursionlimit(10 ** 6)
#st = "abbacbcab"
#st = "BBCDDEDD"
#st = "AAAA"
st ="QWERTYTREWQWERT"[::-1]
#st ="QWERTYTREWQWERTREWQ"
#st = "ABCDEFGH"
#st = "BBCDDECAECBDABADDCEBACCCBDCAABDBADBCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCABCDDECAECBDABADDCEBACCCBDCADBBCDDECAECBDABADDCEBACCCBDCAABDBBBCDDECAECBDABADDCEBACCCBDCAABDBBBCDDECAECBDABADDCEBACCCBDCAABDB"
#print(len(st))
st = input()
def chk(s, left, right, memo):
    while left < right:
        if memo[right][left]:
            return memo[right][left]
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

l = len(st)

tf_arr = [[False]*l for i in range(l)]
dp = [[0]*l for i in range(l)]

for i in range(len(st)):
    width = l-i

    for j in range(i):
        #print(j, width+j)
        tf = chk(st, j, j+width, tf_arr)
        tf_arr[j+width][j] = tf
        dp[j+width][j] = 1 if tf else 0

        #if tf:
        #    print(j,j+width, tf, end ='')
        #else:
        #    print(j,j+width, tf, end ='')

for i in range(len(st)):
    tf_arr[i][i] = True
    dp[i][i] = 1      


"""
for i in range(1,l+1):  
    row = i
    col = 0
    #대각선으로 순회
    for j in range(l - i):  
        #print(f"({row}, {col})", end=" ")
        if dp[row][col] == 0:
            dp[row][col] = i+1
            for k in range(col, row):
                if tf_arr[k][col]:
                    dp[row][col] = min(dp[row][col], dp[k][col]+dp[row][k+1])
                    if dp[row][col] == 2:
                        break

            #dp[row][col]
            #길이 4인 문자열 1+3 2+2 3+1로 분할
            #dp[3][0] =min dp[2][0] +dp[3][3] ,  dp[0][0] + dp[3][1], dp[1][0]+dp[3][2]
            #print("hi:" , i)
        
        row += 1
        col += 1
"""

'''
for i in range(l):
    for j in range(l):
        print(dp[j][i], end = ' ')
    print("")
print("=====================")
'''


for right in range(1,l):
    if not tf_arr[right][0]:
        dp[right][0] = right+1
    # dp[1][0] = min(dp[1][0], dp[0][0]+1)
    # dp[1][0] = min(dp[1][0], dp[1][1]+1)
    # when tf_arr[2][2] is true
    # dp[2][0] = min(dp[2][0], dp[1][0]+1)
    for left in range(1, right+1):
        if tf_arr[right][left]:
            dp[right][0] = min(dp[right][0], dp[left-1][0]+1)


 
#print(dp)
sys.stdout.write(str(dp[l-1][0]))

'''
def partition(s):

    n = len(s)
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    acc = float("inf")

    if n == 1:
        return 1
    else:
        for i in range(1, n):
            #left = s[:i]
            #right = s[i:]
            if is_palindrome(s, 0, i-1):
                dp[0][i-1] = 1
            else:
                pass
                #partition(left)
            if is_palindrome(s, i, n-1):
                #print(n-1)
                #print(i)
                dp[i][n-1] = 1
            else:
                pass
                #partition(right)
    
    for i in range(1,n):
        print(acc)
        acc = min(acc, dp[0][i-1]+dp[i][n-1])
    return acc
    #dp[0][n-1]
'''



