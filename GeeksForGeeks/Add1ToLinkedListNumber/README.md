# Add 1 to a Number Represented as Linked List

### URL:
[Add 1 to a Number Represented as Linked List](https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=add-1-to-a-number-represented-as-linked-list)

## Approach

### Solution 1: String Conversion Approach

1. **Extract Number from Linked List**:
   - Traverse the linked list to extract the number as a string.
   - Convert the string representation into an integer.
   - Increment the integer by 1.
   - Convert the incremented integer back to a string to update the linked list.

2. **Update the Linked List**:
   - Traverse the linked list again and update the node values with the new number.
   - If the new number has more digits than the original, adjust the node values accordingly.

### Solution 2: Reversing the Linked List

1. **Reverse the Linked List**:
   - Reverse the linked list to simplify addition operations.

2. **Perform Addition**:
   - Traverse the linked list and add 1 to the least significant digit.
   - Handle carry propagation.
   - If an extra digit is required, create a new node.

3. **Restore Original Order**:
   - Reverse the linked list back to its original order.

## Complexity

- **Time Complexity**:
  - $$O(n)$$, where $$n$$ is the number of nodes in the linked list. Each node is visited at most twice.

- **Space Complexity**:
  - $$O(1)$$, as no extra space is used apart from variables for traversal and carry handling.

