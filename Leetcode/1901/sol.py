class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        ans = [-1, -1]

        found = [0]
        for idx in range(len(mat)):

            self.binSearch(mat, idx, ans, 0, len(mat[idx]) - 1, found)
            if found[0]:
                break

        return ans

    def binSearch(self, mat, row, ans, low, high, found):

        if low > high:
            return

        mid = (low + high) // 2

        left = True
        right = True
        up = True
        down = True

        if row - 1 >= 0 and mat[row - 1][mid] > mat[row][mid]:
            up = False

        if row + 1 < len(mat) and mat[row + 1][mid] > mat[row][mid]:
            down = False

        if mid + 1 < len(mat[row]) and mat[row][mid + 1] > mat[row][mid]:
            right = False

        if mid - 1 >= 0 and mat[row][mid - 1] > mat[row][mid]:
            left = False

        if up and down and left and right:
            ans[0] = row
            ans[1] = mid

            found[0] = 1

            return

        self.binSearch(mat, row, ans, mid + 1, high, found)
        self.binSearch(mat, row, ans, low, mid - 1, found)



