class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q, level = deque([root]), 0
        max_level = 0
        max_sum = float('-inf')

        while q:
            nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            current_sum = sum(nodes)
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level

        return max_level