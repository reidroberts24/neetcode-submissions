class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # only considering cells with a number?
        ROWS = len(board)
        COLS = len(board[0])

        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        block_sets = defaultdict(set)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                block_index = (i//3, j//3)
                value = board[i][j]
                if (value in row_sets[i] 
                    or value in col_sets[j]
                    or value in block_sets[block_index]):
                    return False

                row_sets[i].add(value)
                col_sets[j].add(value)
                block_sets[block_index].add(value)
        return True