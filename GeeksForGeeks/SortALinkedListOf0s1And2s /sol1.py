class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):

        if not head:
            return head

        count0 = 0
        count1 = 0
        count2 = 0

        cur = head

        while cur:

            if cur.data == 0:
                count0 += 1

            elif cur.data == 1:
                count1 += 1

            else:
                count2 += 1

            cur = cur.next

        cur = head

        while cur:

            if count0 > 0:
                cur.data = 0
                count0 -= 1


            elif count1 > 0:
                cur.data = 1
                count1 -= 1

            else:
                cur.data = 2
                count2 -= 1

            cur = cur.next

        return head