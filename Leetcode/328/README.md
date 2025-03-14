# Odd Even Linked List

### URL:
[Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

## Intuition
The goal is to group all nodes with odd indices together followed by nodes with even indices while preserving the relative order inside both groups. The problem must be solved in **O(1) extra space** and **O(n) time complexity**.

## Approach
1. **Initialization**:
   - We maintain two pointers: `odd` pointing to the first node and `even` pointing to the second node.
   - We also store a reference to the `even` head, so we can append the even list at the end of the odd list.

2. **Iterate through the list**:
   - Traverse the list, linking `odd` nodes together and `even` nodes together.
   - Move `odd` to `odd.next.next` and `even` to `even.next.next` to maintain the grouping.

3. **Merge Odd and Even Lists**:
   - After traversing the list, append the even list to the end of the odd list.

## Complexity
- **Time Complexity**: $$O(n)$$
  - We traverse the linked list once, so the time complexity is linear.
- **Space Complexity**: $$O(1)$$
  - We only use a few extra pointers and do not allocate additional memory proportional to input size.

