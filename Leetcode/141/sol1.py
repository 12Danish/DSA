# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        track = {head}

        temp = head

        while temp.next:

            if temp.next in track:
                return True

            track.add(temp.next)

            temp = temp.next

        return False

