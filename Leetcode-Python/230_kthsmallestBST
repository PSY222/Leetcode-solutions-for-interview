class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def inorder(rt):
        #     return inorder(rt.left) + [rt.val] + inorder(rt.right) if r else []
        # return inorder(root)[k-1]

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right