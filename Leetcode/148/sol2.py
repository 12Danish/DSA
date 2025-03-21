# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            head = self.mergeSort(head)

        return head

    def mergeSort(self, cur):

        middle, last = self.getMiddle(cur)

        if middle == last:
            return cur

        rightptr = middle.next
        leftptr = cur

        last.next = None
        middle.next = None

        leftptr = self.mergeSort(leftptr)
        rightptr = self.mergeSort(rightptr)

        return self.merge(leftptr, rightptr)

    def getMiddle(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if not fast.next:
            return slow, fast

        else:
            return slow, fast.next

    def merge(self, leftptr, rightptr):
        cur = None
        temp = None

        while leftptr and rightptr:

            if leftptr.val <= rightptr.val:

                if not temp:
                    temp = leftptr
                    cur = leftptr

                else:
                    temp.next = leftptr
                    temp = leftptr
                leftptr = leftptr.next

            else:

                if not temp:
                    temp = rightptr
                    cur = rightptr

                else:
                    temp.next = rightptr
                    temp = rightptr

                rightptr = rightptr.next

        while leftptr:
            temp.next = leftptr
            temp = leftptr
            leftptr = leftptr.next

        while rightptr:
            temp.next = rightptr
            temp = rightptr
            rightptr = rightptr.next

        return cur




