class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        for row in range(n):
            self.reverse(matrix[row], n - 1)

    def reverse(self, row, n):
        for y in range(n // 2 + 1):
            temp = row[y]
            row[y] = row[n - y]
            row[n - y] = temp



