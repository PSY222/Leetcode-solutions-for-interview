# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque([root])
        res = []
        IsEven = False
        while q:
            level = []
            IsEven = True if not IsEven else False
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not IsEven:
                res.append(level[::-1])
            else:
                res.append(level)

        return res

#Shorter version
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res, level = [], [root]
        IsEven = False
        
        while root and level:
            l_vals = [node.val for node in level]
            res.append(l_vals if not IsEven else l_vals[::-1])
            level = [kid for n in level for kid in (n.left,n.right) if kid]
            IsEven = True if not IsEven else False
        return res