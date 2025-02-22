# Search in Linked List

### URL:
[Search in Linked List](https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=search-in-linked-list-1664434326)

## General Idea:

The problem requires searching for a given key in a singly linked list. The function should return `True` if the key exists in the linked list, otherwise return `False`.

## Approach:

1. If the linked list is empty (`head == None`), return `False`.
2. Initialize a temporary pointer `temp = head`.
3. Traverse the linked list while `temp` is not `None`:
   - If `temp.data` matches the key, return `True`.
   - Move `temp` to the next node.
4. If the loop ends without finding the key, return `False`.

### Steps:

1. Check if `head` is `None`, return `False`.
2. Iterate through the linked list:
   - Compare each node’s data with `key`.
   - If found, return `True`.
   - Otherwise, continue traversing.
3. If the key is not found, return `False`.

### Complexity Analysis:

1. Time Complexity: O(N)O(N) (We traverse the linked list once)
2. Space Complexity: O(1)O(1) (Only a temporary pointer is used, no extra space)