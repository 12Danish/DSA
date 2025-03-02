# Reverse Linked List

### URL:
[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## General Idea:

The problem requires reversing a given singly linked list. This means modifying the `next` pointers of each node so that they point to the previous node instead of the next one. The head of the original list becomes the tail, and the last node becomes the new head.

---

## Approach 1: Iterative Reversal (Sol1)

This approach involves iterating through the linked list while adjusting the `next` pointers of each node to point to the previous node.

### Steps:
1. Initialize `prev_node` as `None` (this will be the new head).
2. Use a pointer `temp` to iterate through the list.
3. For each node:
   - Store the next node in `next_node` before modifying the pointer.
   - Reverse the `next` pointer of the current node to point to `prev_node`.
   - Move `prev_node` to the current node.
   - Move `temp` to the next node.
4. Return `prev_node` as the new head of the reversed list.

### Time Complexity:
The time complexity is: $$O(N)$$ since each node is visited once.

### Space Complexity:
The space complexity is: $$O(1)$$ as no extra space is used.

---

## Approach 2: Recursive Reversal (Sol2)

This approach involves using recursion to reach the last node and then reversing the pointers as the recursive calls return.

### Steps:
1. Base Case: If the current node is the last node (i.e., `cur.next is None`), update the head reference and return the node.
2. Recursive Step: Call the function for `cur.next` to reach the last node.
3. Reverse the Pointer: Set `cur.next.next = cur` to reverse the link.
4. Ensure the new tail points to `None` by explicitly setting `head.next = None` after recursion completes.
5. Return the new head stored in a mutable reference (`last_node[0]`).

### Time Complexity:
The time complexity is: $$O(N)$$ since each node is visited once.

### Space Complexity:
The space complexity is: $$O(N)$$ due to the recursive call stack.
