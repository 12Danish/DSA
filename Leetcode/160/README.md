## Intersection of Two Linked Lists

### URL

[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

### Intuition

The problem requires finding the intersection node of two singly linked lists. There are multiple ways to solve this problem efficiently.

### Approach 1: Hash Set

1. Traverse the first linked list and store each node in a hash set.
2. Traverse the second linked list and check if any node exists in the set.
3. If found, return that node; otherwise, return `None`.

### Approach 2: Two Pointers

1. Compute the lengths of both linked lists.
2. Calculate the difference in lengths and advance the pointer of the longer list by that difference.
3. Traverse both lists together until a common node is found.
4. If no intersection exists, return `None`.

### Complexity Analysis

- **Time Complexity:**
  - **Hash Set Approach:** \(O(m + n)\), where `m` and `n` are the lengths of the two linked lists.
  - **Two Pointers Approach:** \(O(m + n)\), since we traverse each list at most twice.

- **Space Complexity:**
  - **Hash Set Approach:** \(O(m)\) or \(O(n)\) for storing nodes in a set.
  - **Two Pointers Approach:** \(O(1)\), as no extra space is used.