# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxPath = float("-inf")
        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(0, left)
            right = max(0, right)

            currentPath = left + node.val + right

            maxPath = max(maxPath, currentPath)

            return node.val + max(left, right)
        dfs(root)
        return maxPath