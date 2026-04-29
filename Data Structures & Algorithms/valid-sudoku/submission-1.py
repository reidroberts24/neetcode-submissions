class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # VALIDATE ROWS
        for i in range(9):
            cur_row = set()
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                if item in cur_row:
                    return False
                cur_row.add(item)

        # VALIDATE COLS
        for i in range(9):
            cur_col = set()
            for j in range(9):
                item = board[j][i]
                if item in cur_col:
                    return False
                elif item != ".":
                    cur_col.add(item)

        # VALIDATE BOXES

        starts = [(0,0),(0,3),(0,6),(3,0),(6,0),(3,3),(3,6),(6,3),(6,6)]
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
        return True