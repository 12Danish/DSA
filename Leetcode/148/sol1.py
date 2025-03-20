# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        head = self.sortLL(head)

        return head

    def sortLL(self, curNode):

        if not curNode.next:
            return curNode

        prevNode = self.sortLL(curNode.next)

        if curNode.val <= prevNode.val:
            curNode.next = prevNode

            return curNode


        else:
            temp = prevNode

            while temp.next and curNode.val > temp.next.val:
                temp = temp.next

            curNode.next = temp.next

            temp.next = curNode

            return prevNode



