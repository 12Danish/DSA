# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        temp = head
        count = 1
        cur_head = None 
        prev = None

        while temp:
            if count == 1:
                cur_head = temp

            if count / k == 1:
               
                next = temp.next
                nf, ne = self.reverse(cur_head,k)
                if prev:
                  
                    prev.next = nf

                ne.next = next

                prev = ne
                temp = ne
                if  cur_head == head:
    
                    head = nf
                            
            count += 1
            temp = temp.next

            if count > k:
                count = 1
        
        return head

                     
    def reverse(self, start,k):
     
        temp = start
        prev = None 

        for x in range(k):
           
            next = temp.next
            if not prev:
                temp.next = None 

            else:
                temp.next = prev

            prev = temp
            temp = next
        
           
        return prev, start
