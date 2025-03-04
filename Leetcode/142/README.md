## Linked List Cycle II

### Url

[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

## Intuition

The problem requires determining whether a linked list contains a cycle and returning the node where the cycle begins. A cycle exists if a node can be revisited by continuously following the `next` pointer. To detect cycles efficiently, we use the approach:

### Tortoise and Hare Approach (Two Pointers)

1. Use two pointers: `slow` moves one step at a time, and `fast` moves two steps.
2. If `fast` catches up to `slow`, a cycle is detected.
3. Once a cycle is detected, reset `slow` to `head` and move both `slow` and `fast` one step at a time.
4. The node where they meet is the start of the cycle.
5. If `fast` reaches `None`, return `None` (no cycle).

### Complexity

- **Time Complexity:** \(O(n)\), as each node is visited at most twice.
- **Space Complexity:** \(O(1)\), since only two pointers are used.









