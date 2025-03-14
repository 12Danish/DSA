# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        temp = head.next

        while odd and even and odd.next.next and even.next.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next

            even = even.next

        if odd.next.next:
            odd.next = odd.next.next

            odd = odd.next

        even.next = None

        odd.next = temp

        return head











