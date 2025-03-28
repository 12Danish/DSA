# Segregate 0s, 1s, and 2s in a Linked List

### URL:
[Segregate 0s, 1s, and 2s in a Linked List](https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=given-a-linked-list-of-0s-1s-and-2s-sort-it)

## General Idea:
The problem requires sorting a linked list where each node contains only 0, 1, or 2. The objective is to modify the linked list such that all 0s appear first, followed by 1s, and all 2s appear at the end.

## Approach:
### Approach 1: Counting Sort
1. **Traverse the linked list** to count the occurrences of 0s, 1s, and 2s.
2. **Modify the linked list** by overwriting the values based on the counts in sorted order.

### Approach 2: Three-Pointer Method
1. **Create three dummy nodes** to store separate lists for 0s, 1s, and 2s.
2. **Traverse the list** and link nodes to their respective lists.
3. **Merge the three lists** to get the final sorted linked list.

## Steps:
### Approach 1 (Counting Sort):
1. Traverse the list and count occurrences of 0, 1, and 2.
2. Re-traverse the list and update the node values based on the counts.

### Approach 2 (Three-Pointer Method):
1. Create three dummy nodes for 0s, 1s, and 2s.
2. Traverse the original list and link each node to the corresponding list.
3. Merge the three lists in the correct order and update the head.

### Complexity Analysis:
- **Time Complexity:** O(N) (Single pass traversal for both approaches)
- **Space Complexity:**
  - **Counting Sort:** O(1) (Modifies the list in place)
  - **Three-Pointer Method:** O(1) (Uses only extra pointers)

