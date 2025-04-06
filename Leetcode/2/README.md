# Add Two Numbers

### URL:
[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

# Intuition
The problem gives two non-empty linked lists representing two non-negative integers where the digits are stored in reverse order. Each node contains a single digit, and we are to return their sum as a new linked list in the same reversed order. The natural approach is to traverse both lists simultaneously, adding corresponding digits along with any carry from the previous step, and constructing the result list on the fly.

# Approach
1. Initialize two pointers, one for each list (`ptr1` and `ptr2`), a `carry` variable set to 0, and `head` and `prev` pointers to build the result list.
2. Traverse both lists simultaneously:
   - Add the values of the current nodes and the carry.
   - Create a new node with the digit part (`res % 10`) and attach it to the result list.
   - Update carry as `res // 10`.
3. Once one of the lists is exhausted, continue with the remaining list while still considering the carry.
4. If there's any carry left after the traversal, add an extra node with that value.
5. Return the head of the new linked list.

# Complexity
- Time complexity:  
  The time complexity is $$O(\max(n, m))$$, where $$n$$ and $$m$$ are the lengths of the two input linked lists. We iterate through both lists once.

- Space complexity:  
  The space complexity is $$O(\max(n, m))$$ since we create a new node for each digit in the longer of the two lists, plus potentially one extra node if there is a carry at the end.
