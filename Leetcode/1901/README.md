# Find a Peak Element II  

### URL:  
[Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/description/)  

## General Idea:  

The problem requires finding a **peak element** in a **2D matrix**, where a peak is strictly greater than its adjacent neighbors (left, right, top, bottom). The entire matrix is considered to be surrounded by `-1`.  

To solve this efficiently in **O(m log(n))** or **O(n log(m))**, we use a **binary search approach**:  

- Perform **binary search** on columns, selecting the middle column.  
- Find the **maximum element** in that column.  
- Check if this element is a peak by comparing it to its adjacent elements.  
- If it is not a peak, move to the left or right half of the matrix based on where a greater element exists.  
- Repeat the process recursively until a peak is found.  

## Time Complexity:  

The time complexity is **O(m log(n))** or **O(n log(m))**, depending on whether we perform binary search on columns or rows first.  

## Space Complexity:  

The space complexity is **O(1)** since only a constant amount of extra space is used.  
