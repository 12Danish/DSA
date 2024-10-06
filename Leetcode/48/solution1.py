class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        cm = [[0] * (len(matrix)) for _ in range(len(matrix))]

        cur_col = len(matrix) - 1

        for row in matrix:

            for idx, entry in enumerate(row):
                cm[idx][cur_col] = entry
            cur_col -= 1

        matrix.clear()
        matrix[:] = cm