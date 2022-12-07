def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            
            sum = l1val + l2val + carry
            
            carry = sum//10
            new = ListNode(sum%10)
            curr.next = new
            curr = new
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next