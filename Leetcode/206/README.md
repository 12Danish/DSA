# Reverse Linked List

### URL:
[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## General Idea:

The problem requires reversing a given singly linked list. This means modifying the `next` pointers of each node so that they point to the previous node instead of the next one. The head of the original list becomes the tail, and the last node becomes the new head.

## Approach: Iterative Reversal

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

