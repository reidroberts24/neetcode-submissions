class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1) + 1, len(text2) + 1
        dp = [[0 for j in range(COLS)] for i in range(ROWS)]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[ROWS - 1][COLS - 1]