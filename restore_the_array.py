t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    a = [0] * n
    a[0] = arr[0]
    
    for i in range(1, n-1):
        a[i] = min(arr[i-1], arr[i])
    
    a[-1] = arr[-1]
    
    print(*a)
