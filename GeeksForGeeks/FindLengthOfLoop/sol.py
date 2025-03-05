# User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):

        slow = head
        fast = head
        count = 0

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 2
                fast = fast.next
                while fast.next != slow:
                    fast = fast.next
                    count += 1

                return count

        return 0
