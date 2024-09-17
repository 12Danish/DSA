# Leaders in an Array

### URL:
[Leaders in an Array](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array)

## Approach
1. **Initialization**:
   - Create an empty list `leaders` to store the leader elements.
   - Initialize `max` with the last element of the array (`arr[n-1]`) since the last element is always a leader.

2. **Iterate through the array from right to left**:
   - Traverse the array in reverse order starting from the second-to-last element:
     - If the current element is greater than or equal to `max`, it is a leader. 
     - Update `max` to the current element.
     - Insert the current element at the start of the `leaders` list.

3. **Return Result**:
   - After processing all elements, the `leaders` list will contain all the leader elements in the correct order.

## Complexity
- **Time complexity**: 
  - The algorithm runs in linear time, so the time complexity is $$O(n)$$, where $$n$$ is the length of the array `arr`.

- **Space complexity**: 
  - The space complexity is $$O(1)$$ (excluding the space required for the result list) because no extra space is used other than the output list.
