
class Solution:
    def addTwoNumbers(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ptr1 = l1

        ptr2 = l2

        carry = 0

        head = None

        prev = None

        while ptr1 and ptr2:

            res = ptr1.val + ptr2.val
            if carry > 0:
                res += carry

            newNode = ListNode(res % 10)
            if not head:
                head = newNode

            if prev:
                prev.next = newNode

            prev = newNode

            carry = res // 10

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:

            res = ptr1.val

            if carry > 0:
                res += carry

            newNode = ListNode(res % 10)

            if prev:
                prev.next = newNode

            prev = newNode

            carry = res // 10

            ptr1 = ptr1.next

        while ptr2:

            res = ptr2.val

            if carry > 0:
                res += carry

            newNode = ListNode(res % 10)

            if prev:
                prev.next = newNode

            prev = newNode
            carry = res // 10
            ptr2 = ptr2.next

        if carry:
            newNode = ListNode(carry)
            prev.next = newNode
            prev = newNode
            carry = 0

        return head



