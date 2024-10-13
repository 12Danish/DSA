class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        # Create a deep copy of the matrix
        matrix_copy = [row[:] for row in matrix]
        spiral = []
        row = 0
        col = 0
        mcl = len(matrix_copy)
        mcr = len(matrix_copy[0])
        while matrix_copy:
            # Move right across the top row
            mcl = len(matrix_copy)
            mcr = len(matrix_copy[0])

            while col < mcr:
                spiral.append(matrix_copy[row][col])
                col += 1

            # Remove the top row after processing
            matrix_copy.pop(0)
            col -= 1

            if not matrix_copy:
                break

            mcl = len(matrix_copy)

            # Move down the rightmost column
            while row < mcl:
                spiral.append(matrix_copy[row][col])
                row += 1

            # Remove the last column from all rows
            for i in range(mcl):
                matrix_copy[i].pop()

            print(matrix_copy)
            for i in range(mcl):
                print(i)
                try:
                    if not matrix_copy[i]:
                        del matrix_copy[i]
                except:
                    if matrix_copy:
                        del matrix_copy[i % len(matrix_copy)]
                        continue
                    else:
                        break
            print(matrix_copy)
            if not matrix_copy:
                break

            mcl = len(matrix_copy)
            mcr = len(matrix_copy[0])

            row = mcl - 1
            col -= 1

            # Move left across the bottom row
            while col >= 0:
                spiral.append(matrix_copy[row][col])
                col -= 1

            # Remove the bottom row after processing
            matrix_copy.pop()

            if not matrix_copy:
                break
            mcl = len(matrix_copy)
            row = mcl - 1  # Adjust row position for moving up
            col = 0  # Reset column to the leftmost position

            # Move up the leftmost column
            while row >= 0:
                spiral.append(matrix_copy[row][col])
                row -= 1

            # Remove the first column from all rows

            for i in range(mcl):
                matrix_copy[i].pop(0)

            for i in range(mcl):
                try:
                    if not matrix_copy[i]:
                        del matrix_copy[i]
                except:
                    if matrix_copy:
                        del matrix_copy[i % len(matrix_copy)]
                        continue
                    else:
                        break

            if not matrix_copy:
                break
            row = 0  # Reset row position
            col = 0  # Reset column position

        return spiral
