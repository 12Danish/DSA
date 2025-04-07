# Delete All Occurrences of a Given Key in a Doubly Linked List

### URL:
[Delete All Occurrences of a Given Key in a Doubly Linked List](https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list)

## General Idea:

The problem requires removing all nodes from a doubly linked list that contain a specific value (`key`). The task is to traverse the list and remove every node that matches the key while maintaining the structural integrity of the doubly linked list.

## Approach:

1. Traverse the doubly linked list from the head.
2. For each node, check if the node's data matches the given key.
3. If a match is found:
   - Adjust the previous node’s `next` pointer.
   - Adjust the next node’s `prev` pointer.
   - Handle edge cases when the node to delete is the head, tail, or the only node in the list.
4. Continue traversal to the next node even after deletion.
5. Return the updated head of the list.

### Steps:

1. Initialize a pointer `temp` to the head of the doubly linked list.
2. Iterate through the list while `temp` is not `None`:
   - If `temp.data` equals the key:
     - If the node is the only element, update `head` to `None`.
     - If it is the head node, update `head` and remove `prev` link of the new head.
     - If it is the tail node, set `prev.next` to `None`.
     - Otherwise, connect `prev.next` to `next` and `next.prev` to `prev`.
   - Move to the next node.
3. Return the updated `head`.

### Complexity Analysis:

1. **Time Complexity:** O(N)  
   - Each node is visited once.

2. **Space Complexity:** O(1)  
   - No extra space is used apart from a few pointers.
