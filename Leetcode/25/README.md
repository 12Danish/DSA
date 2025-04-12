
# Reverse Nodes in k-Group  
https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Intuition  
When scanning the list, we need to reverse every `k` consecutive nodes. But if there are fewer than `k` nodes left at the end, they should remain unchanged. Instead of modifying node values, we change the actual node pointers, so we’ll need to carefully reverse sublists of size `k` and reconnect them correctly.

# Approach  
- Traverse the list with a pointer and keep a count.
- For every group of `k` nodes:
  - Use a helper function to reverse those `k` nodes.
  - Reconnect the reversed group with the previous part of the list and with the rest of the list.
  - Keep track of the new head and tail of the reversed part to continue processing.
- If the remaining nodes are fewer than `k`, leave them as is.

We define a `reverse(start, k)` helper method to reverse exactly `k` nodes and return the new head and tail.

# Complexity  
- Time complexity:  
  $$O(n)$$  
  We traverse each node once and reverse in chunks of `k`.

- Space complexity:  
  $$O(1)$$  
  We do in-place reversal, using constant extra space.

