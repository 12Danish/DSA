# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        leng = 1
        temp = head
        while temp.next:
            temp = temp.next
            leng += 1

        steps = leng - n

        if steps == 0:

            if leng == 1:
                head = None
            else:
                head = head.next

            return head

        temp = head

        for x in range(1, steps):
            temp = temp.next

        temp.next = temp.next.next

        return head


