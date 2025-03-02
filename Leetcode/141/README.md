## Linked List Cycle

### Url

[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

## Intuition

The problem requires determining whether a linked list contains a cycle. A cycle exists if a node can be revisited by continuously following the `next` pointer. To detect cycles efficiently, we use two approaches:

## Approach 1: HashSet (Visited Nodes)

1. Use a HashSet to store visited nodes.
2. Traverse the linked list, checking if the current node is already in the set.
3. If a node is revisited, return `True` (cycle detected).
4. If the traversal reaches `None`, return `False` (no cycle).

### Complexity

- **Time Complexity:** \(O(n)\), where \(n\) is the number of nodes in the linked list. We traverse each node once.
- **Space Complexity:** \(O(n)\), as we store visited nodes in a HashSet.

## Approach 2: Tortoise and Hare Approach(Two Pointers)

1. Use two pointers: `slow` moves one step at a time, and `fast` moves two steps.
2. If `fast` catches up to `slow`, a cycle is detected.
3. If `fast` reaches `None`, return `False` (no cycle).

### Complexity

- **Time Complexity:** \(O(n)\), as each node is visited at most twice.
- **Space Complexity:** \(O(1)\), since only two pointers are used.

call the second approach tortoie and ahre approach





