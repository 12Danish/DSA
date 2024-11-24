# Merge Intervals

### URL:
[Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## Approach 1:

### Intuition
Iterate through the intervals, keeping track of merged intervals using a set to avoid duplicate processing. This approach focuses on a two-pointer technique to identify and merge overlapping intervals.

### Approach
1. **Sort the Intervals**:
   - Sort the intervals based on their starting times.
2. **Merge Overlapping Intervals**:
   - Use two pointers to compare and merge overlapping intervals.
3. **Track Merged Intervals**:
   - Use a set to avoid redundant processing and ensure unique merged intervals.

### Complexity
- **Time Complexity**: $$O(n^2)$$ due to nested iterations for merging intervals.
- **Space Complexity**: $$O(n)$$ for storing merged intervals and tracking indices.

---

## Approach 2:

### Intuition
Leverage sorting to simplify the merging process. As the intervals are sorted, overlap checking becomes straightforward by comparing the current interval’s end with the next interval’s start.

### Approach
1. **Sort the Intervals**:
   - Sort the intervals based on their start times.
2. **Iterate and Merge**:
   - For each interval, check if it overlaps with the last merged interval. If it does, merge them; otherwise, add it as a new interval.

### Complexity
- **Time Complexity**: $$O(n \log n)$$ for sorting and $$O(n)$$ for iterating, making it $$O(n \log n)$$ overall.
- **Space Complexity**: $$O(n)$$ for storing merged intervals.

---

## Approach 3:

### Intuition
Use a temporary interval to track the current merging state. If the current interval overlaps with the temporary interval, merge them; otherwise, store the temporary interval and update it.

### Approach
1. **Sort the Intervals**:
   - Sort intervals by their starting times.
2. **Iterate Through Intervals**:
   - Initialize a temporary interval with the first interval.
   - For each subsequent interval, merge it with the temporary interval if it overlaps. Otherwise, store the temporary interval and update it.
3. **Add the Last Interval**:
   - After the loop, append the remaining temporary interval to the result.

### Complexity
- **Time Complexity**: $$O(n \log n)$$ for sorting and $$O(n)$$ for merging, resulting in $$O(n \log n)$$ overall.
- **Space Complexity**: $$O(n)$$ for storing merged intervals.
