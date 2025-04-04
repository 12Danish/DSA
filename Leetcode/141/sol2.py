# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:

            if slow != head or fast != head:

                fast = fast.next.next

                if fast == slow:
                    return True

                slow = slow.next

                if slow == fast:
                    return True

            else:
                slow = slow.next

                if not slow:
                    return False

                if slow == fast:
                    return True

                fast = fast.next.next

        return False

