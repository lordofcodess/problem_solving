N, X = map(int, input().split())
subjects = []

for i in range(X):
    y = map(float,input().split())
    subjects.append(y)

for scores in zip(*subjects):
    avg = sum(scores) / X
    print(avg)
