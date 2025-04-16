# Rotate List

### URL:
[Rotate List](https://leetcode.com/problems/rotate-list/description/)

## Approach 1:

### Intuition
To rotate a linked list to the right by `k` places, we can observe that the last `k` nodes will become the new head, and the remaining nodes will follow. However, to achieve this efficiently, we must consider the list's length and handle cases where `k` is greater than the length.

### Approach
1. **Edge Case Check**:
   - If the list is empty or `k` is 0, return the head as is.
2. **Calculate Length**:
   - Traverse the linked list once to find its length.
   - Compute `k % length` to handle cases where `k` exceeds the list length.
   - If the result is 0, the list remains unchanged.
3. **Reverse Entire List**:
   - Reverse the entire linked list.
4. **Reverse First `k` Nodes**:
   - After full reversal, reverse the first `k` nodes again to restore their order.
5. **Reverse Remaining Nodes**:
   - Reverse the rest of the list after the first `k` nodes.
6. **Reattach and Return**:
   - Attach the reversed remaining part to the tail of the first reversed segment and return the new head.

### Complexity
- **Time Complexity**: $$O(n)$$ — We traverse the list multiple times (for length calculation and reversals).
- **Space Complexity**: $$O(1)$$ — All operations are done in-place without extra space.
