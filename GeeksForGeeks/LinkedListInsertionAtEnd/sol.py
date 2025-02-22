'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''


class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):

        new_node = Node(x)

        if not head:
            head = new_node
            return head

        temp = head
        while temp.next:
            temp = temp.next

        temp.next = new_node

        return head

