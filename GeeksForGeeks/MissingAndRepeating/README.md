# Find Missing and Repeating

### URL:
[Find Missing and Repeating](https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-missing-and-repeating)

## Approach
1. **Approach 1: Using Set**:
   - Traverse the array while keeping track of elements already seen using a set.
   - Identify the repeating element during traversal.
   - Use another loop to find the missing element by checking for numbers not present in the set.

2. **Approach 2: Using Mathematical Formula**:
   - Use the sum of first \(n\) natural numbers and the sum of their squares.
   - Compute the difference between the expected sums and the actual sums to derive equations for the missing and repeating numbers.
   - Solve the equations to find the missing and repeating numbers efficiently.

## Complexity Analysis
1. **Approach 1: Using Set**:
   - **Time Complexity**: 
     - \(O(n)\) for traversing the array and checking the set.
   - **Space Complexity**: 
     - \(O(n)\) for maintaining the set of numbers.

2. **Approach 2: Using Mathematical Formula**:
   - **Time Complexity**: 
     - \(O(n)\) for a single traversal of the array.
   - **Space Complexity**: 
     - \(O(1)\), as no extra space is used apart from variables for calculations.
