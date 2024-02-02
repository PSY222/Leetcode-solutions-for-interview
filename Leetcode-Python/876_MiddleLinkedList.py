# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = turn = 0
        while curr:
            curr = curr.next
            length += 1
        curr = head
        
        if length %2 == 0:
            mid = (length//2)+1
        else:
            mid = (length+1)//2
            
        while head:
            turn += 1
            if turn == mid:
                return head
            head = head.next

#Smart solution Source: https://leetcode.com/problems/middle-of-the-linked-list/discuss/1651600/PythonJavaC%2B%2B-Simple-Solution-oror-One-Pass-oror-Beginner-Friendly-oror-Detailed-Explanation
class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
