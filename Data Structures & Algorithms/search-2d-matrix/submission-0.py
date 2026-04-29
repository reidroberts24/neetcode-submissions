class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find which row the target would be in
        # binary search that row to see if it exists
        def search_row(row):
            l, r = 0, len(row) - 1
            while l <= r:
                m = (r + l) // 2
                if row[m] < target:
                    l = m + 1
                elif row[m] > target:
                    r = m - 1
                else:
                    return True
            return False

        Lrow, Rrow = 0, len(matrix) - 1
        while Lrow <= Rrow:
            Mrow = (Lrow + Rrow) // 2
            if matrix[Mrow][0] <= target and target <= matrix[Mrow][-1]:
                return search_row(matrix[Mrow])
            elif matrix[Mrow][0] > target:
                Rrow = Mrow - 1
            elif matrix[Mrow][0] < target:
                Lrow = Mrow + 1
        return False


        