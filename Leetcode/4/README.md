# Median of Two Sorted Arrays

### URL:
[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

# Intuition
The problem requires us to find the median of two sorted arrays in **O(log (m+n))** time complexity. Since the median is the middle element (or the average of two middle elements for an even-length array), we need an efficient way to merge and find this middle element.

A brute force approach would be merging the two arrays and then finding the median, but this takes **O(m + n)** time and extra space. Instead, we can leverage **binary search** to achieve the optimal time complexity.

# Approach

### **Approach 1: Merge and Find Median (O(m + n) Time, O(m + n) Space)**
1. Merge both sorted arrays into a new list.
2. Use two pointers to iterate and merge elements while maintaining sorted order.
3. If the merged list length is odd, return the middle element.
4. If even, return the average of the two middle elements.

### **Approach 2: Two Pointers without Extra Space (O(m + n) Time, O(1) Space)**
1. Instead of creating a merged array, track only the necessary middle elements.
2. Use two pointers (`p1` for `nums1` and `p2` for `nums2`) to traverse until reaching the median position.
3. Maintain the last two elements needed for median calculation.
4. If the total length is odd, return the last element. Otherwise, return the average of the last two.

### **Approach 3: Binary Search on the Smaller Array (O(log(min(m, n))) Time, O(1) Space)**
1. Perform binary search on the smaller array to find a partition that divides both arrays into two halves such that:
   - The left half contains elements **≤** all elements in the right half.
2. Define partition indices `mid1` and `mid2` such that:
   - `left1 <= right2` and `left2 <= right1`
3. If the partition is valid, return the median based on the combined array length.
4. Otherwise, adjust the search range and repeat.

# Complexity

- **Time Complexity:**
  - Approach 1: **O(m + n)**
  - Approach 2: **O(m + n)**
  - Approach 3: **O(log(min(m, n)))**

- **Space Complexity:**
  - Approach 1: **O(m + n)** (Extra space for merged array)
  - Approach 2: **O(1)** (No extra space)
  - Approach 3: **O(1)** (Binary search, constant space)
