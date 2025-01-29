N = int(input())  
arr = list(map(int, input().split()))  

acc = [0]*N

for i in range(N):
    acc[i] = max(acc[i-1]+arr[i] , arr[i])
print(max(acc))
