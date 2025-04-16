# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head 

        temp = head 

        prev = None 

        ll_len = 0

        while temp:
            temp = temp.next
            ll_len +=1 
        
        k = k % ll_len
        if k == 0:
            return head 
        
        temp = head


        while temp:

            next = temp.next

            if prev :
                temp.next = prev 
            
            else:
                temp.next = None 
            
            prev = temp 
            temp = next 
        
        head  = prev 

        temp = head
        ptr1 = head 
        prev = None 

        for x in range(k):
       
            if not temp:
                break 
            next = temp.next

            if prev :
                temp.next = prev 
            
            else:
                temp.next = None 
            
            prev = temp 
            temp = next 

        
        head = prev 
  

        prev = None 
        while temp:
            next = temp.next

            if prev :
                temp.next = prev 
            
            else:
                temp.next = None 
            
            prev = temp 
            temp = next 

        
        ptr1.next = prev

        return head 



