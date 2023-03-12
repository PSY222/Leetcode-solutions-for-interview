# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists.pop()
        if not lists:
            return
    
        def mergeTwoLists(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            
            if list1.val < list2.val:
                next_val = list1.next
                list1.next = mergeTwoLists(next_val,list2)
                return list1
            else:
                next_val = list2.next
                list2.next = mergeTwoLists(list1,next_val)
                return list2
        

        mid = len(lists)//2
        l,r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return mergeTwoLists(l,r)

#Solution2
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(head.val,i,head) for i, head in enumerate(lists) if head]
        hq.heapify(heap)
        dummy = ListNode(0)
        curr= dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next :
                heappop(heap)
            else:
                heapreplace(heap,(node.next.val,i,node.next))
            curr.next = node
            curr = curr.next
        return dummy.next
        