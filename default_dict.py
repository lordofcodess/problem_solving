from collections import defaultdict

n, m = map(int, input().split())

groupA = []
for _ in range(n):
    word = input()
    groupA.append(word)

groupB = []
for _ in range(m):
    word = input()
    groupB.append(word)


indices = defaultdict(list)
for i, word in enumerate(groupA):
    indices[word].append(i + 1)  


for word in groupB:
    if word in indices:
        print(' '.join(map(str, indices[word])))
    else:
        print(-1)
