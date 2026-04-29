class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, path_length):
            if path_length == len(word):
                return True
            if (i >= ROWS or i < 0 or j >= COLS or j < 0 or
                board[i][j] == "#" or
                board[i][j] != word[path_length]):
                return False
            
            board[i][j] = "#"
            
            res = (dfs(i + 1, j, path_length + 1) or
                    dfs(i - 1, j, path_length + 1) or
                    dfs(i, j + 1, path_length + 1) or
                    dfs(i, j - 1, path_length + 1))
            board[i][j] = word[path_length]
            return res

        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False