# Linked List Insertion

### URL:
[Linked List Insertion](https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=linked-list-insertion)

## Approach
1. **Overview**:
   - The problem requires inserting a given value `x` at the end of a **singly linked list** and returning the modified linked list.
   - A new node is created with the given value and added at the end of the list.

2. **Steps**:
   - Create a new node with the value `x`.
   - If the linked list is empty (`head` is `None`), return the new node as the head.
   - Otherwise, traverse the list using a temporary pointer `temp` until the last node is found.
   - Set the `next` pointer of the last node to the newly created node.
   - Return the updated head of the linked list.

3. **Complexity Analysis**:
   - **Time Complexity**:
     - Traversing the list takes \(O(n)\) time in the worst case, where \(n\) is the number of nodes.
   - **Space Complexity**:
     - Since no extra space is used apart from the new node, the space complexity is \(O(1)\).
