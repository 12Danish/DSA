# Introduction to Linked List

### URL:
[Introduction to Linked List](https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-linked-list)

## Approach
1. **Initialization**:
   - Define three pointers: `head` (to store the head of the linked list), `new_node` (to create new nodes), and `prev_node` (to keep track of the previous node).
   
2. **Iterate through the array**:
   - Loop through each element in `arr`:
     - Create a new `Node` using the current element.
     - If `head` is `None`, assign `new_node` to `head` (first node).
     - If `prev_node` exists, link it to `new_node`.
     - Update `prev_node` to `new_node` for the next iteration.

3. **Return Result**:
   - After iterating through the array, return `head`, which points to the first node of the constructed linked list.

## Complexity
- **Time complexity**:
  - The algorithm runs in linear time, so the time complexity is $$O(n)$$, where $$n$$ is the length of the array `arr`.

- **Space complexity**:
  - The space complexity is $$O(n)$$ because we are creating `n` nodes for the linked list, each taking additional memory.

