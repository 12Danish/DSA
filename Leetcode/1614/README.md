# Maximum Nesting Depth of the Parentheses

### URL:
[Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/)

## Intuition
The goal is to determine the maximum depth of nested parentheses in a valid parentheses string. The depth is defined as the maximum number of open parentheses `(` encountered at any point before being closed.

## Approach
1. **Use a Stack to Track Parentheses**:
   - Maintain a stack to keep track of open parentheses `(`.
   - Whenever an open parenthesis is encountered, push it onto the stack.
   - When a closing parenthesis `)` is found, pop from the stack.

2. **Track Maximum Nesting Depth**:
   - At each step, update a variable `max_val` to store the maximum size of the stack, which represents the deepest level of nesting.

3. **Return the Maximum Depth**:
   - After processing all characters, `max_val` holds the maximum depth of nested parentheses.

## Complexity
- **Time Complexity**: $$O(n)$$
  - We traverse the string once, performing push and pop operations on the stack.
- **Space Complexity**: $$O(n)$$
  - In the worst case (all open parentheses before closing), the stack stores $$O(n)$$ elements.
