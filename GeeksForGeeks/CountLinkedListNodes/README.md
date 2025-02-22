# Count Nodes of Linked List

### URL:
[Count Nodes of Linked List](https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=count-nodes-of-linked-list)

## General Idea:

The problem requires counting the number of nodes in a singly linked list. The length of the linked list is defined as the total number of nodes present in it.

## Approach:

1. Initialize a counter variable `count = 0`.
2. Traverse the linked list starting from `head`.
3. For each node encountered, increment the counter by `1`.
4. Once the traversal reaches the end (`None`), return the counter value.

### Steps:

1. If `head` is `None`, return `0` (empty list).
2. Initialize `count = 0` and `temp = head`.
3. Iterate through the linked list while `temp` is not `None`:
   - Increment `count`.
   - Move `temp` to the next node.
4. Return `count` after exiting the loop.

###  Complexity Analysis:

1. Time Complexity: O(N)O(N) (We traverse each node exactly once)
2. Space Complexity: O(1)O(1) (Only a counter variable is used, no extra space)