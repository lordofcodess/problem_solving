n = int(input())
s = list(map(int, input().split()))
 
t_sum = sum(s)
arr = []
 
for i in range(n):
    remaining_sum = t_sum - s[i]
    if remaining_sum / (n - 1) == s[i]:
        arr.append(i + 1)
 
count = len(arr)
print(count)
if count > 0:
    print(" ".join(map(str, arr)))
