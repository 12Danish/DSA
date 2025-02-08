# Remove Outermost Parentheses

### URL:
[Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)

## Intuition
The problem requires us to remove the outermost parentheses from every **primitive** valid parentheses string in `s`. A primitive valid parentheses string is a non-empty valid substring that cannot be split further into smaller valid parentheses strings.

To solve this, we need to track the nesting level of parentheses while iterating through `s`. The first opening parenthesis `(` of a primitive and the last closing `)` of a primitive should be removed.

## Approach
1. **Use a Stack Approach (Implicit Counter)**:
   - Use a counter `stack` to track the depth of valid parentheses.
   - Iterate over `s`, updating `stack` accordingly:
     - If `x == '('`, increase `stack` (entering a deeper level).
     - If `x == ')'`, decrease `stack` (closing a level).
   - Append characters to the result **only if they are not the outermost parentheses**.
   - When `stack == 0`, it means we completed a primitive, so we reset tracking.

2. **Concatenate Valid Parts**:
   - Whenever `stack == 0`, we extract the valid part excluding outermost parentheses and add it to the result.

## Complexity
- **Time Complexity**: $$O(n)$$, where `n` is the length of `s`, as we traverse the string once.
- **Space Complexity**: $$O(1)$$, since we use a few extra variables, but our answer string does not count as extra space.

