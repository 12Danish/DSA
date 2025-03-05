# Find Length of Loop in a Linked List

### URL:
[Find Length of Loop](https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop)

## Approach
1. **Overview**:
   - The problem requires determining if a linked list contains a loop.
   - If a loop exists, return the number of nodes in the loop; otherwise, return `0`.

2. **Steps**:
   - Use **Floyd’s Cycle Detection Algorithm (Tortoise and Hare)**:
     - Initialize two pointers: `slow` and `fast`, both starting at `head`.
     - Move `slow` one step at a time, while `fast` moves two steps.
     - If `slow` and `fast` meet, a loop exists.
   - To determine the loop's length:
     - Keep moving `fast` forward until it meets `slow` again.
     - Count the number of steps taken to complete one cycle.

3. **Complexity Analysis**:
   - **Time Complexity**: \(O(n)\) — The loop detection and counting run in linear time.
   - **Space Complexity**: \(O(1)\) — Only two pointers are used, requiring constant space.
