class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos_set = set()
        zer_row = set()

        for idx1, x in enumerate(matrix):
            for idx2, y in enumerate(x):
                if y == 0:
                    pos_set.add(idx2)
                    zer_row.add(idx1)

        for pos in pos_set:
            for arr in matrix:
                arr[pos] = 0

        for row in zer_row:
            matrix[row] = [0] * len(matrix[row])


