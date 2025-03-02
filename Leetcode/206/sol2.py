# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        last_node = [head]

        self.reverse(head, last_node)

        head.next = None
        return last_node[0]

    def reverse(self, cur, last_node):

        if not cur.next:
            last_node[0] = cur
            return cur

        prev_node = self.reverse(cur.next, last_node)

        prev_node.next = cur

        return cur




