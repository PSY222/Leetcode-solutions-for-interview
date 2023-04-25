# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],  minv = float('-inf'), maxv =float('inf')) -> bool:
        
        if not root: return True
        
        if minv >= root.val or root.val >= maxv:
            return False
        return self.isValidBST(root.left,minv,root.val) and self.isValidBST(root.right,root.val,maxv)
                
        #DFS