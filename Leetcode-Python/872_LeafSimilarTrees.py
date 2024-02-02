class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.helper(root1) == self.helper(root2)

    def helper(self,root):
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            res.append(root.val)
        res += self.helper(root.left)
        res += self.helper(root.right)
        return res
