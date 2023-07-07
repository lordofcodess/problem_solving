class Solution(object):
    def isValidSudoku(self, board):

        rowarr = [set() for i in range(9)]
        colarr = [set() for i in range(9)]
        boxarr = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                
                if cell in colarr[j]:
                    return False
                colarr[j].add(cell)

                if cell in rowarr[i]:
                    return False
                rowarr[i].add(cell)
                
                # Check sub-box
                box_idx = (i // 3) * 3 + j // 3
                if cell in boxarr[box_idx]:
                    return False
                boxarr[box_idx].add(cell)

        return True
