# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        temp = headA
        ans = None

        while temp:
            seen.add(temp)
            temp = temp.next

        temp = headB

        while temp:
            if temp in seen:
                ans = temp
                return ans

            temp = temp.next

        return ans