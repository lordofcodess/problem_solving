seq = [1]
while seq[-1] < 10**18:
	seq.append(seq[-1]*2)

seq.pop()

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	print(n)
	for i in range(n):
		print(i+1, min([j for j in seq if a[i] <= j]) - a[i])
