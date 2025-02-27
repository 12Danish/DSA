# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        temp = head

        ll_len = 1

        while temp.next:
            temp = temp.next

            ll_len += 1

        print(ll_len)
        mid_len = ceil(ll_len / 2) if ll_len % 2 != 0 else (ll_len / 2) + 1

        print(mid_len)
        temp = head

        count = 1

        while count < mid_len:
            temp = temp.next
            count += 1

        return temp




