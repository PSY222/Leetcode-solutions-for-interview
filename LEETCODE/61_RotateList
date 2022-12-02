# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        curr= prev= head
        lgth = self.length(head)
        
        if k == 0 or lgth ==1:
            return curr
        
        k %= lgth
        
        while curr.next:
            prev = curr
            curr = curr.next
        curr.next = head
        prev.next = None
        return self.rotateRight(curr,k-1)
    
    def length(self,head):
        curr = head
        cnt = 0
        while curr:
            curr = curr.next
            cnt +=1
        return cnt
            