# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        diff = 0
        temp = headA

        while temp:
            lenA += 1
            temp = temp.next

        temp = headB

        while temp:
            lenB += 1
            temp = temp.next

        diff = abs(lenA - lenB)

        temp1 = headA
        temp2 = headB

        if lenA < lenB:

            for x in range(diff):
                temp2 = temp2.next

        elif lenB < lenA:

            for x in range(diff):
                temp1 = temp1.next

        while temp1 and temp2:

            if temp1 == temp2:
                return temp1

            temp1 = temp1.next
            temp2 = temp2.next

        return None



