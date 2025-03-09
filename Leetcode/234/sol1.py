# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        stack = []

        temp = head

        ll_len = 0

        while temp:
            ll_len += 1

            temp = temp.next

        if ll_len == 1:
            return True

        mid = ceil(ll_len / 2)

        odd = True if ll_len % 2 != 0 else False

        temp = head
        count = 0
        while temp:

            if count < mid - 1:
                stack.append(temp.val)

            elif count == mid - 1:
                if not odd:
                    stack.append(temp.val)

            else:

                el = stack.pop()

                if el != temp.val:
                    return False

            count += 1
            temp = temp.next

        return True



