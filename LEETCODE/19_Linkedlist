# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lgh = self.length(head)
        curr = head
        
        if lgh == n:
            return head.next
        
        for i in range(lgh-n-1):
            curr = curr.next
        
        curr.next = curr.next.next    
                
        return head
    
    def length(self,head):
        temp = head
        cnt = 0
        while temp:
            cnt +=1
            temp = temp.next
        return cnt

          
        
            