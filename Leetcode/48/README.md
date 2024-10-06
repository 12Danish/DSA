# Rotate Image

### URL:
[Rotate Image](https://leetcode.com/problems/rotate-image/)

## Approach 1:

### Intuition
To rotate a matrix by 90 degrees clockwise, the primary approach is to transpose the matrix (swap elements across the diagonal) and then reverse each row. This in-place method efficiently rotates the matrix without using extra space.

### Approach
1. **Transpose the Matrix**:
   - Transposing involves converting rows to columns. For each element in the upper triangular part of the matrix, we swap it with its corresponding element across the diagonal.
   - Specifically, for each element `matrix[row][col]`, swap it with `matrix[col][row]` for `col > row`.

2. **Reverse Each Row**:
   - After transposing the matrix, reverse the elements in each row to complete the 90-degree clockwise rotation.

### Complexity
- Time complexity: $$O(n^2)$$
  - The algorithm involves two steps: transposing and reversing rows in an `n x n` matrix, which takes quadratic time.

- Space complexity: $$O(1)$$
  - Since the matrix is modified in-place, no extra space is required.

## Approach 2:

### Intuition
This approach involves creating a new matrix and copying the rotated version of the input matrix into it. After creating the new matrix, we copy its contents back into the original matrix. However, this solution uses extra space.

### Approach
1. **Create a New Matrix**:
   - Construct a new matrix `cm` of the same size as the input matrix.
   - For each element in the original matrix, map it to its new position in the rotated matrix. The element `matrix[row][col]` in the original matrix will map to `cm[col][n - 1 - row]` in the new matrix.

2. **Copy the New Matrix to the Original Matrix**:
   - Clear the original matrix and replace its contents with the newly constructed matrix using shallow copies.

### Complexity
- Time complexity: $$O(n^2)$$
  - Copying elements into the new matrix and then back into the original matrix takes quadratic time.

- Space complexity: $$O(n^2)$$
  - An additional `n x n` matrix is created, requiring extra space.
