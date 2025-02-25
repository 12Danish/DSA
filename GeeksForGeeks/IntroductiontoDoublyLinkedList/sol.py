# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None



class Solution:
    def constructDLL(self, arr):

        head = None
        prev_node = None

        for x in arr:

            new_node = Node(x)

            if not head:
                head = new_node

            if prev_node:
                prev_node.next = new_node
                new_node.prev = prev_node


            prev_node = new_node


        return head
