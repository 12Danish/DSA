# String to Integer (atoi)

### URL:
[LeetCode - String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

# Intuition
The problem requires converting a given string into a **32-bit signed integer** following specific rules:
1. **Ignore leading whitespaces**.
2. **Determine the sign** (`+` or `-`). If absent, assume positive.
3. **Extract numeric characters** until a non-digit is encountered.
4. **Clamp the result** within the range **[-2³¹, 2³¹ - 1]**.
5. **Return the final integer**.

A straightforward approach is to iterate over the string, extracting valid numeric characters, converting them into an integer, and ensuring it stays within the valid range.

# Approach

### **Approach: Iterative Parsing and Conversion (O(n) Time, O(1) Space)**
1. **Trim leading whitespaces** using `.strip()`.
2. **Check for sign (`+` or `-`)** and store it.
3. **Extract numeric characters** while they are valid digits.
4. **Convert the extracted number into an integer**.
5. **Clamp the value** to stay within the **32-bit integer range**.
6. **Return the final integer**.

# Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the input string.
- **Space Complexity:** `O(1)`, as no extra data structures are used.

