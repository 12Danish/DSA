## Sort List

### Url

[Sort List](https://leetcode.com/problems/sort-list/)

## Intuition

The problem requires sorting a linked list in ascending order. Since the input is a linked list, algorithms like **Merge Sort** and **Insertion Sort** are more suitable due to their efficiency in linked list operations.

### Approach 1: Recursive Insertion Sort

1. Traverse the list recursively until the base case (single node or empty list).
2. Recursively sort the rest of the list.
3. Insert the current node at the correct position in the sorted part.
4. Return the head of the sorted list.

### Approach 2: Merge Sort

1. Use the **fast and slow pointer technique** to find the middle of the list.
2. Recursively split the list into two halves until each sublist has a single node.
3. Merge the two sorted halves back together.
4. Return the sorted linked list.

### Complexity

- **Time Complexity:**
  - **Recursive Insertion Sort:** \(O(n^2)\), as each element needs to be placed correctly.
  - **Merge Sort:** \(O(n \log n)\), since we recursively divide the list and merge it back.

- **Space Complexity:**
  - **Recursive Insertion Sort:** \(O(1)\) (in-place sorting).
  - **Merge Sort:** \(O(\log n)\) due to recursive calls.

