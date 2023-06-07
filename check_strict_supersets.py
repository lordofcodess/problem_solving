setA = set(map(int, input().split()))
n = int(input())
is_superset = True

for _ in range(n):
    setB = set(map(int, input().split()))
    if not setB.issubset(setA):
        is_superset = False
        break

print(is_superset)
