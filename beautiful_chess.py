t = int(input()) 
result = []

for n in range(t):
    input()
    chessboard = [input() for n in range(8)] 

    for i in range(1, 7):  
        for j in range(1, 7): 
            if chessboard[i][j] == '#':
                if chessboard[i-1][j-1] == '#' and chessboard[i+1][j+1] == '#' and chessboard[i-1][j+1] == '#' and chessboard[i+1][j-1] == '#':
                    result.append(i+1)
                    result.append(j+1)
                    break

for i in range(0, len(result), 2):
    if i + 1 < len(result):
        print(result[i], result[i + 1])
