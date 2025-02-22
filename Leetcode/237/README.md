# Delete Node in a Linked List

### URL:
[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)

## General Idea:

The problem requires deleting a node from a singly linked list **without** access to the head. The given node is guaranteed **not to be the tail** of the list.

## Approach:

1. Since we don't have access to the previous node, we **cannot** perform a standard delete operation.
2. Instead, we **copy the value of the next node** into the given node.
3. Then, we **update the next pointer** to skip the next node, effectively removing it.

### Steps:

1. If `node` is `None` or `node.next` is `None`, return (though the problem guarantees `node` is not the last).
2. Copy `node.next.val` into `node.val`.
3. Update `node.next` to `node.next.next`.

