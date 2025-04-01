


class Solution:
    def addOne(self, head):

        if not head:
            return

        if head.next:
            head = self.reverseLL(head)

        carry = 0

        temp = head

        last = temp

        while temp:

            if temp.data + 1 > 9:
                temp.data = 0
                carry = 1

            else:
                temp.data += 1
                carry = 0
                break

            if not temp.next:
                last = temp

            temp = temp.next

        if carry:
            new_node = Node(1)

            last.next = new_node

        head = self.reverseLL(head)

        return head

    def reverseLL(self, cur):
        prev = None

        while cur:
            next = cur.next

            if prev:

                cur.next = prev

                prev = cur


            else:
                cur.next = None

                prev = cur

            cur = next

        return prev

