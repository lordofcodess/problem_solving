a = int(input())
 
for i in range(a):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
 
    for j in range(1, n):
        if arr[j - 1] > arr[j]:
            answer += 1
 
    if answer != n - 1:
        print("YES")
    else:
        print("NO")
