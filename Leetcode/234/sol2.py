class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # Empty list or single node is a palindrome

        # Find middle using slow and fast pointers
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second_half_head = self.reverseList(slow.next)
        ptr1 = head
        ptr2 = second_half_head

        slow.next = None
        pal = True

        while ptr1 and ptr2:

            if ptr1.val != ptr2.val:
                pal = False
                break

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        orig_second_half_head = self.reverseList(second_half_head)
        slow.next = orig_second_half_head

        return pal

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # Store next pointer before changing it
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev forward
            curr = next_temp  # Move curr forward

        return prev  # prev is now the new head



