# Spiral Matrix

### URL:
[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The goal of the problem is to return all the elements of a matrix in spiral order. This means starting from the top-left corner, traversing the top row, then the rightmost column, the bottom row, the leftmost column, and continuing inward in this pattern. My first thought was to simulate this traversal by systematically removing the processed rows and columns while adding their elements to a result list.

## Approach
<!-- Describe your approach to solving the problem. -->
1. **Matrix Copy:** Start by making a deep copy of the matrix to preserve the original structure.
2. **Traverse in Spiral:** 
   - Begin at the top-left corner and traverse the top row from left to right.
   - Move down the rightmost column.
   - Traverse the bottom row from right to left.
   - Move up the leftmost column.
3. **Remove Processed Rows/Columns:** After traversing the edges, remove the corresponding rows and columns to shrink the matrix.
4. **Repeat:** Continue the spiral traversal on the remaining matrix until no elements are left.

By following this approach, each element of the matrix is added to the result list in the correct spiral order.

## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(m \times n)$$, where $$m$$ is the number of rows and $$n$$ is the number of columns in the matrix. Each element is visited exactly once.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $$O(m \times n)$$, as we create a copy of the matrix and store the result list.

## Code
```python3 []
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        # Create a deep copy of the matrix
        matrix_copy = [row[:] for row in matrix]
        spiral = []
        row = 0
        col = 0

        while matrix_copy:
            mcl = len(matrix_copy)
            mcr = len(matrix_copy[0])

            # Move right across the top row
            while col < mcr:
                spiral.append(matrix_copy[row][col])
                col += 1

            matrix_copy.pop(0)
            col -= 1

            if not matrix_copy:
                break
            mcl = len(matrix_copy)

            # Move down the rightmost column
            row = 0
            while row < mcl:
                spiral.append(matrix_copy[row][col])
                row += 1

            for i in range(mcl):
                matrix_copy[i].pop()
            
            row = mcl - 1
            col -= 1

            if not matrix_copy:
                break

            # Move left across the bottom row
            while col >= 0:
                spiral.append(matrix_copy[row][col])
                col -= 1

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

            for i in range(mcl):
                matrix_copy[i].pop(0)

        return spiral
