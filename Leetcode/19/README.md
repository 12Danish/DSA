# Remove Nth Node From End of List

### URL
[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

## Problem Description
Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

## Intuition
The problem requires removing the `n`th node from the end of a singly linked list. Instead of iterating twice (once to find the length and once to remove the node), an efficient approach is to use the **two-pointer technique** to locate the target node in a single pass.

## Approach
1. **Use Two Pointers**:  
   - Maintain two pointers: `first` and `second`, both initially pointing to the head.
   - Move the `first` pointer `n` steps ahead.
2. **Move Both Pointers**:  
   - Move both pointers one step at a time until `first` reaches the end.
   - At this point, `second` will be just before the node that needs to be removed.
3. **Remove the Target Node**:  
   - Adjust the `next` pointer of `second` to skip the target node.
   - If `n` is equal to the length of the list, remove the head by returning `head.next`.

## Complexity
- **Time Complexity**:  
  \(O(L)\), where \(L\) is the length of the linked list, as we traverse it at most once.

- **Space Complexity**:  
  \(O(1)\), since only two pointers are used.
